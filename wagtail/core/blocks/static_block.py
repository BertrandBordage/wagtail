from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from .base import Block

__all__ = ['StaticBlock']


class StaticBlock(Block):
    """
    A block that just 'exists' and has no fields.
    """
    def render_form(self, value, prefix='', errors=None):
        if self.meta.admin_text is None:
            if self.label:
                return _('%(label)s: this block has no options.') % {'label': self.label}
            else:
                return _('This block has no options.')
        return self.meta.admin_text

    def value_from_datadict(self, data, files, prefix):
        return None

    @cached_property
    def definition(self):
        definition = Block.definition.func(self)
        definition.update(
            isStatic=True,
            html=self.render_form(self.get_default(),
                                  prefix=self.FIELD_NAME_TEMPLATE),
        )
        return definition

    class Meta:
        admin_text = None
        default = None
