from rest_framework import permissions


class GlobalDefaultpermission(permissions.BasePermission):
    # Sobrescrever o método has_permission
    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )
        if not model_permission_codename:
            return False
        return request.user.has_perm(model_permission_codename)  # verifica se o usuário tem a permissão

    # função para montagem da string genérica
    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name  # vem o nome do model
            app_label = view.queryset.model._meta.app_label  # vem o nome da app
            action = self.__get_action_sufix(method)  # busca no de-para qual a ação está vindo
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    # Função que mapeia os métodos
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
