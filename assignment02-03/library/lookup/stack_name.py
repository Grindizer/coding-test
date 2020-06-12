from ansible.plugins.lookup import LookupBase
from ansible.utils import py3compat


class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):
        ansible_env = variables.get('ansible_env')
        ansible_app = variables.get('ansible_app')
        return [f'{ansible_env}-{ansible_app}-{term}'
                for term in terms]
