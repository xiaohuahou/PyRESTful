from rest_framework.schemas import AutoSchema

class CreditSchema(AutoSchema):

    def _allows_filters(self, path, method):
        """
                Determine whether to include filter Fields in schema.

                Default implementation looks for ModelViewSet or GenericAPIView
                actions/methods that cause filtering on the default implementation.

                Override to adjust behaviour for your view.

                Note: Introduced in v3.7: Initially "private" (i.e. with leading underscore)
                    to allow changes based on user experience.
                """
        if getattr(self.view, 'filter_backends', None) is None:
            return False

        if hasattr(self.view, 'action'):
            return self.view.action in ["list"] #only allow list filters

        return method.lower() in ["get", "put", "patch", "delete"]