import _plotly_utils.basevalidators


class X0Validator(_plotly_utils.basevalidators.AnyValidator):

    def __init__(self, plotly_name='x0', parent_name='layout.shape', **kwargs):
        super(X0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calcIfAutorange+arraydraw',
            role='info',
            **kwargs
        )
