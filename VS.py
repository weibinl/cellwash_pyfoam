import sys 
sys.path.append("/usr/lib/freecad/lib")
FREECADPATH='/usr/lib/freecad/lib'
def import_fcstd(path_freecad):
    #function to import the FreeCAD module
    sys.path.append('/usr/lib/freecad/lib')
    import FreeCAD
    try:
        import FreeCAD as FreeCAD
    except:
        print "Could not import FreeCAD"
        print "Are you using the right path"

import_fcstd(FREECADPATH)
freecad_doc_name='python_scrit_test'
freecad_doc_path='/home/weibin/vs/'
freecad_extension='.fcstd' 
# extension to use when sae freecad file

working_doc=FreeCAD.newDocument(freecad_doc_name)
cylinder_1=working_doc.addObject('Part::Cylinder','cylinder_1')
cylinder_1.Radius=4
working_doc.saveAs(freecad_doc_path+freecad_doc_name+freecad_extension)