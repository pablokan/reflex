
import os
import importlib
"""
ruta = os.path.join('mp', 'pages')
archivos = os.listdir(ruta)
archivos = ['.' + name[:-3] for name in archivos if not name.startswith('_')]
print('archivos de init:', archivos)

for m in archivos:
    # Quitamos el punto inicial para la importación
    module_name = f"mp.pages{m}"
    # Importamos el módulo
    importlib.import_module(module_name)
"""
from .index import index
from .dos import dos
from .cinco import cinco

uno_module = importlib.import_module('.uno', package='mp.pages')
uno = getattr(uno_module, 'uno')



