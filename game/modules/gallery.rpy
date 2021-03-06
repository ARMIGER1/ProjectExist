screen glossary:
    # This ensures that any other menu screen is replaced.
    tag menu

    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5
        xmaximum 800
        ymaximum 500
        vbox:    
            textbutton "Characters" xminimum 300 action ShowMenu("characters")
            #textbutton "RPG/Battle System" xminimum 300 action ShowMenu("bat_sys_dir")
            textbutton "Return" xminimum 300 action ShowMenu("more_menu")
    
screen bat_sys_dir:
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5
        xmaximum 800
        ymaximum 500
        
        vbox:
            textbutton "Moves" xminimum 300 action ShowMenu("moves")
            textbutton "FP" xminimum 300 action ui.callsinnewcontext("about_fp")
            textbutton "SP" xminimum 300 action ui.callsinnewcontext("about_sp")
            textbutton "Time of Day" xminimum 300 action ui.callsinnewcontext("about_tod")
            textbutton "Return" action ShowMenu("glossary")
            bar adjustment adj style "vscrollbar"
 
screen moves:
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5
        xmaximum 800
        ymaximum 500
        
        vbox:
            textbutton "Return" action Return()
            bar adjustment adj style "vscrollbar"
            
screen characters:
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5
        xmaximum 800
        ymaximum 500
        
        vbox:
            textbutton "Kazuki Okamoto" xminimum 300 action ui.callsinnewcontext("about_char", "kazuki")#
            textbutton "Katherine \"Rin\" Faust" xminimum 300 action ui.callsinnewcontext("about_char", "katherine")#
            
            textbutton "Professor Lawrence" xminimum 300 action ui.callsinnewcontext("about_char", "proflaw")#
            textbutton "Jonathan Gravano" xminimum 300 action ui.callsinnewcontext("about_char", "jonathan")#
            textbutton "Natalie Bellangerd" xminimum 300 action If(persistent.seen_natalie, ui.callsinnewcontext("about_char", "natalie"))#
            textbutton "William \"Wil\" Nolan" xminimum 300 action If(persistent.seen_wil, ui.callsinnewcontext("about_char", "wil"))
            textbutton "Tamara \"Tammy\" Mirov" xminimum 300 action If(persistent.seen_tamara, ui.callsinnewcontext("about_char", "tammy"))#
            textbutton "Lilian Crawford" xminimum 300 action If(persistent.seen_lilian, ui.callsinnewcontext("about_char", "lilian"))#
            
            textbutton "Athena" xminimum 300 action If(persistent.seen_athena, ui.callsinnewcontext("about_char", "athena"))#
            textbutton "Gorō Nyūdō Masamune" xminimum 300 action If(persistent.seen_masamune, ui.callsinnewcontext("about_char", "masamune"))#
            textbutton "Ultraman 7" xminimum 300 action ui.callsinnewcontext("about_char", "ultraman7")#
            textbutton "Ultraman 7" xminimum 300 action If(persistent.seen_ultraman, ui.callsinnewcontext("about_char", "ultraman7"))#
            textbutton "Return" action ShowMenu("glossary")
            bar adjustment adj style "vscrollbar"

# New CG Gallery Code
#
# Release 2 (2007-03-31)
# http://www.renpy.org/wiki/renpy/doc/cookbook/New_CG_Gallery

init -50 python:

    style.create('gallery_nav_frame', 'frame')
    style.create('gallery_nav_vbox', 'vbox')
    style.create('gallery_nav_button', 'button')
    style.create('gallery_nav_button_text', 'button_text')

    style.gallery_nav_button.size_group = "gallery_nav_button"
    
    class GalleryGridLayout(object):
        def __init__(self, gridsize, upperleft, offsets):
            self.gridsize = gridsize
            self.upperleft = upperleft
            self.offsets = offsets

        def __call__(self, imagenum, image_count):

            cols, rows = self.gridsize
            ulx, uly = self.upperleft
            ox, oy = self.offsets

            return dict(
                xpos = ulx + (imagenum % cols) * ox,
                ypos = uly + (imagenum // cols) * oy,
                )
           
    class GalleryAllPriorCondition(object):

        def check(self, all_prior):
            return all_prior
    
    class GalleryArbitraryCondition(object):
        def __init__(self, condition):
            self.condition = condition

        def check(self, all_prior):
            return eval(self.condition)
                    
    class GalleryUnlockCondition(object):
        def __init__(self, images):
            self.images = images
            
        def check(self, all_prior):
            for i in self.images:
                if tuple(i.split()) not in persistent._seen_images:
                    return False

            return True
            
            
    class GalleryImage(object):
        def __init__(self, gallery, images, displayable):
            self.gallery = gallery
            self.images = images or [ ]
            self.displayable = displayable
            self.conditions = [ ]

        def check_unlock(self, all_prior):
            for i in self.conditions:
                if not i.check(all_prior):
                    return False

            return True
        
        def show_locked(self, image_num, image_count):
            renpy.transition(self.gallery.transition)
            self.gallery.locked_image(image_num, image_count)

            ui.saybehavior()
            ui.interact()
            
        def show(self, image_num, image_count):
            renpy.transition(self.gallery.transition)

            renpy.scene()

            for i in self.images:
                renpy.show(i)

            if self.displayable:
                ui.add(self.displayable)

            ui.saybehavior()
            ui.interact()

            
                    
    class GalleryButton(object):
        def __init__(self, gallery, idle, hover, insensitive, properties):
            self.gallery = gallery
            self.idle = idle
            self.hover = hover
            self.insensitive = insensitive
            self.properties = properties
            self.images  = [ ]
            self.conditions = [ ]
            
        def check_unlock(self):
            for i in self.conditions:
                if not i.check(True):
                    return False
            
            for i in self.images:
                if i.check_unlock(False):
                    return True

            return False
            
        def render(self, i, pos):
            props = pos.copy()
            props.update(self.properties)

            if not self.check_unlock():
                insensitive = self.insensitive or self.gallery.locked_button
                if insensitive is not None:
                    ui.image(insensitive, **props)
                    return

            if self.hover:
                ui.imagebutton(self.idle,
                               self.hover,
                               clicked=ui.returns(("button", i)),
                               **props)
            
            else:
                ui.image(self.idle, **props)
                ui.imagebutton(self.gallery.idle_border,
                               self.gallery.hover_border,
                               clicked=ui.returns(("button", i)),
                               **props)

        def show(self):

            all_prior = True

            for i, img in enumerate(self.images):
                if img.check_unlock(all_prior):
                    img.show(i, len(self.images))
                else:
                    img.show_locked(i, len(self.images))
                    all_prior = False
                
                
    class GalleryPage(object):

        def __init__(self, gallery, name, background):
            self.gallery = gallery
            self.name = name
            self.background = background
            self.buttons = [ ]

            
    class Gallery(object):

        transition = dissolve
        
        locked_button = None
        locked_background = "#000"
                
        hover_border = None
        idle_border = None

        background = None
        
        
        def __init__(self):
            self.pages = [ ]

            self.page_ = None
            self.button_ = None
            self.image_ = None
            self.unlockable = None
            
        def page(self, name, background=None):

            self.page_ = GalleryPage(self, name, background)
            self.pages.append(self.page_)

        def button(self, idle, hover=None, locked=None, **properties):
            self.button_ = GalleryButton(self, idle, hover, locked, properties)
            self.page_.buttons.append(self.button_)
            self.unlockable = self.button_
            
        def image(self, *images):
            self.image_ = GalleryImage(self, images, None)
            self.button_.images.append(self.image_)
            self.unlockable = self.image_

        def display(self, displayable):
            self.image_ = GalleryImage(self, [ ], displayable)
            self.button_.images.append(self.image_)
            self.unlockable = self.image_
            
        def unlock(self, *images):
            self.unlockable.conditions.append(GalleryUnlockCondition(images))

        def condition(self, condition):
            self.unlockable.conditions.append(GalleryArbitraryCondition(condition))

        def allprior(self):
            self.unlockable.conditions.append(GalleryAllPriorCondition())
    
        def unlock_image(self, *images):
            self.image(*images)
            self.unlock(*images)

        def navigation(self, page_name, page_num, pages):

            ui.frame(style='gallery_nav_frame')
            ui.vbox(style='gallery_nav_vbox')

            for i, p in enumerate(self.pages):
                layout.button(p.name,
                              "gallery_nav",
                              selected=(i == page_num),
                              clicked=ui.returns(("page", i)))

            ui.null(height=22)
            layout.button("Return", "gallery_nav", clicked=ShowMenu("more_menu"))

            ui.close()


        def grid_layout(self, gridsize, upperleft, offsets):
            self.layout = GalleryGridLayout(gridsize, upperleft, offsets)

        def layout(self, i, n):
            return { }

        def locked_image(self, num, total):
            ui.add(self.locked_background)
            ui.text(_("Image %d of %d is locked.") % (num + 1, total), xalign=0.5, yalign=0.5)
            
        def show(self, page=0):

            
            while True:
                renpy.transition(self.transition)

                p = self.pages[page]
                
                bg = p.background or self.background
                if bg is not None:
                    renpy.scene()
                    ui.add(bg)

                self.navigation(p.name, page, len(self.pages))
                    
                for i, b in enumerate(p.buttons):
                    pos = self.layout(i, len(p.buttons))
                    b.render(i, pos)

                cmd, arg = ui.interact(suppress_overlay=True, suppress_underlay=True)

                if cmd == "return":
                    return

                elif cmd == "page":
                    page = arg
                    continue

                elif cmd == "button":
                    p.buttons[arg].show()
                    continue
                    
init:
    # Position the navigation on the right side of the screen.
    $ style.gallery_nav_frame.xpos = 1200 - 10
    $ style.gallery_nav_frame.xanchor = 1.0
    $ style.gallery_nav_frame.ypos = 12

# The entry point to the gallery code.

label gallery:
    
    python hide:

        # Construct a new gallery object.
        g = Gallery()

        # The image used for locked buttons.
        g.locked_button = "thumbs/thumb_lock.png"

        # The background of a locked image.
        g.locked_background = "drops/failure.png"

        # Frames added over unlocked buttons, in hover and idle states.
        g.hover_border = "thumbs/over.png"
        g.idle_border = "thumbs/over.png"

        # An images used as the background of the various gallery pages.
        g.background = "#C0C0C0"

        # Lay out the gallery images on the screen.
        # These settings lay images out 3 across and 4 down.
        # The upper left corner of the gird is at xpos 10, ypos 20.
        # They expect button images to be 155x112 in size.
        g.grid_layout((3, 4), (10, 12), (160, 115))

        # Show the background page.
        g.page("Backgrounds")

        g.button("thumbs/thumb_fog.png")
        g.unlock_image("bg fog")
        g.button("thumbs/thumb_kaz_bed.png")
        g.unlock_image("bg kazuki bed")
        g.button("thumbs/thumb_kaz_journal.png")
        g.unlock_image("bg kazuki journal")

        #g.button("thumbs/thumb_lock.png")
        #g.unlock_image("bg beach daytime")
        #g.unlock_image("bg fog")
        
        #
        # These show images, if they have been unlocked. The image name must
        # have been defined using an image statement.
        #g.unlock_image("bg beach nighttime")
        #
        # This shows a displayable...
        #g.display("beach_sketch.jpg")
        # ... if all prior images have been show.
        #g.allprior()

        # A second set of images.
        #g.button("thumb_lighthouse.jpg")
        #g.unlock_image("bg lighthouse day")
        #g.unlock_image("bg lighthouse night")
        #g.display("lighthouse_sketch.jpg")
        #g.allprior()



        # We can use g.page to introduce a second page.
        #g.page("Characters")

        #g.button("thumb_eileen.jpg")
        #
        # Note that we can give image and unlock image more than one image
        # at a time.
        #g.unlock_image("bg lighthouse day", "eileen day happy")
        #g.unlock_image("bg lighthouse day", "eileen day mad")



        # Another page, this one for concept art.
        #g.page("Concept Art")

        
       #g.button("thumb_concepts.jpg")
        #
        # We can apply conditions to buttons as well as to images.
        # The "condition" condition checks an arbitrary expression.
        #g.condition("persistent.beat_game")
        #
        #g.display("concept1.jpg")
        #g.display("concept2.jpg")
        #g.display("concept3.jpg")


        # Now, show the gallery.
        g.show()

    return

