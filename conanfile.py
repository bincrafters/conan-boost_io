from conans import ConanFile, tools, os

class BoostIoConan(ConanFile):
    name = "Boost.Io"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/io"
    description = "For a description of this library, please visit http://boost.org/io "
    license = "www.boost.org/users/license.html"
    lib_short_name = "io"
    requires = "Boost.Config/1.64.0@bincrafters/testing"

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = src=os.path.join(os.getcwd(), self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)
