class JBridgeIntroHandler(webapp.RequestHandler):
     def get(self, *args):
        userStatus = UserStatus()
        userStatus = userStatus.getStatus(self.request.uri)

        template_values = {
            'userStatus': userStatus,
            'stylesheets' : ['/assets/css/owl.carousel.css', '/assets/css/owl.theme_original.css'],
            'scripts' : ['/assets/js/owl.carousel.js', '/assets/js/jbridgeintro.js', '/assets/js/ytexpo.js'],
            'courseToModules' : getCoursesAndModules()
        }


        path = os.path.join(os.path.dirname(__file__), 'static_pages/other/jBridgeIntro.html')
        self.response.out.write(template.render(path, template_values))
