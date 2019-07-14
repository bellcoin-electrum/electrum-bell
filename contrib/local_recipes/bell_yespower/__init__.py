from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.toolchain import current_directory
import shutil
import glob

class Bell_YespowerRecipe(CythonRecipe):

    url = 'https://github.com/bellcoin-electrum/bell_yespower_python3/archive/master.zip'

    patches = ['./setup.patch']
    depends = ['setuptools']

#    def build_arch(self, arch):
#        super(Bell_YespowerRecipe, self).build_arch(arch)
#
#        env = self.get_recipe_env(arch)
#        with current_directory(self.get_build_dir(arch.arch)):
#            so_file = glob.glob('./build/lib*/*so')
#            shutil.copyfile(so_file[0], self.ctx.get_libs_dir(arch.arch) + "/bell_yespower.so")

recipe = Bell_YespowerRecipe()
