#---------------------------------------------------------------------------
# Name:        etg/_webkit.py
# Author:      Robin Dunn
#
# Created:     22-Aug-2013
# Copyright:   (c) 2013-2016 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx" 
MODULE    = "_webkit"
NAME      = "_webkit"   # Base name of the file to generate to for this script
DOCSTRING = """\
The :ref:`wx.webkit.wxWebKitCtrl` and related classes are provided mainly for
backwards compatibility only. New code would be more future-proof by using the
``wx.html2`` module.  The classes in this module are light wrappers around
the OSX WebKit control and is not implemented on any other platform.
"""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ ]    
    

# The list of other ETG scripts and back-end generator modules that are
# included as part of this module. These should all be items that are put in
# the wxWidgets "webview" library in a multi-lib build.
INCLUDES = [ 'webkit',
             ]


# Separate the list into those that are generated from ETG scripts and the
# rest. These lists can be used from the build scripts to get a list of
# sources and/or additional dependencies when building this extension module.
ETGFILES = ['etg/%s.py' % NAME] + tools.getEtgFiles(INCLUDES)
DEPENDS = tools.getNonEtgFiles(INCLUDES)
OTHERDEPS = [  ]


#---------------------------------------------------------------------------
 
def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    module.check4unittest = False

    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    module.addHeaderCode('#include <wxpy_api.h>')
    module.addImport('_core')
    module.addPyCode('import wx', order=10)
    module.addInclude(INCLUDES)
 

    #-----------------------------------------------------------------
    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)
    

    
#---------------------------------------------------------------------------

if __name__ == '__main__':
    run()
