from .widgets import *

# Register a comm target for Javascript initialized widgets..
from IPython import get_ipython
ip = get_ipython()
if ip is not None and hasattr(ip, 'kernel') and hasattr(ip.kernel, 'comm_manager'):
    ip.kernel.comm_manager.register_target('ipython.widget', Widget.handle_comm_opened)
