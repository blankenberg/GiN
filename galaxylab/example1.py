from ipywidgets import VBox, widget_serialization
from traitlets import Unicode, List, Dict, Instance
from ._frontend import module_name, module_version
from nbtools.basewidget import BaseWidget
import bioblend
from bioblend.galaxy.objects import *


class GalaxyTools(BaseWidget):
    """
    Widget used to render Python output in a UI
    """
    _model_name = Unicode('GalaxyToolModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)

    _view_name = Unicode('GalaxyToolView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    name = Unicode('pdaug tsvtofasta').tag(sync=True)
    File = Unicode('File Name').tag(sync=True)
    status = Unicode('').tag(sync=True)
    files = List(Unicode, []).tag(sync=True)
    text = Unicode('').tag(sync=True)
    visualization = Unicode('').tag(sync=True)
    appendix = Instance(VBox).tag(sync=True, **widget_serialization)
    extra_file_menu_items = Dict().tag(sync=True)
    
    # gi = GalaxyInstance("http://localhost:8080", email="jaidev53ster@gmail.com", api_key="b6b0868d4c27b745be2bd68d04c1c213", verify=True)
    # a = bioblend.galaxy.objects.client.ObjToolClient(gi)
    # tool = a.get(id_='toolshed.g2.bx.psu.edu/repos/jay/pdaug_peptide_sequence_analysis/pdaug_peptide_sequence_analysis/0.1.0',  io_details=True)

    # gi = GalaxyInstance("http://localhost:8080", email="jaidev53ster@gmail.com", api_key="b6b0868d4c27b745be2bd68d04c1c213", verify=True)
    # a = bioblend.galaxy.objects.client.ObjToolClient(gi)
    # tool = a.get(id_='vcf_to_maf_customtrack1',  io_details=True)

    # inputs = tool.wrapped['inputs']
    # inputs = List(inputs).tag(sync=True)

    def __init__(self, **kwargs):
        # Initialize the child widget container
        self.appendix = VBox()
        BaseWidget.__init__(self, **kwargs)