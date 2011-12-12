from Acquisition import aq_inner
from AccessControl.SecurityManagement import getSecurityManager

from plone.app.layout.viewlets import ViewletBase

class MultilingualContentViewlet(ViewletBase):

    def update(self):
        # We have to check the view permission on the translated object, because
        # getTranslations returns all objects, no matter the workflow state
        context = aq_inner(self.context)
        current = context.Language()
        _checkPermission = getSecurityManager().checkPermission
        self.translations = []
        try:
            for lang, content in context.getTranslations(review_state=False).items():
                if lang != current and _checkPermission('View', content):
                    self.translations.append(content)
        except AttributeError:
            # Handle the situation for site-root templates.
            # Plone site root has not translations
            pass

            
    


        
