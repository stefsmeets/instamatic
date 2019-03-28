from . import sed_frame
from . import cred_frame
from . import cred_tvips_frame
from . import io_frame
from . import red_frame
from . import ctrl_frame
from . import debug_frame
from . import about_frame
from . import machine_learning_frame
from . import autocred_frame
from . import FEI_RotationCmder

MODULES = (
io_frame.module,
cred_frame.module,
cred_tvips_frame.module,
FEI_RotationCmder.module,
autocred_frame.module,
sed_frame.module,
red_frame.module,
ctrl_frame.module,
machine_learning_frame.module,
debug_frame.module,
about_frame.module,
)
