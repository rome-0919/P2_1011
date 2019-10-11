import os
from facename import *
# file_path = r"C:\Users\hz4eyb\Desktop\pas"
# file_name = "t1_V1_190912"
# cad_file = r"C:\Users\hz4eyb\Desktop\pas\1test_p"


def import_scdoc(file_path, scdoc_file):
    message = r"""
file/set-tui-version "19.1"
file/import/cad-options/extract-features yes 15
file/import/cad-geometry yes %s/%s no 
m cfd-surface-mesh no 0.0015 0.006 1.25 yes yes 10 3 faces-and-edges yes no
diagnostics/face-connectivity/fix-free-faces face-zones *() merge-nodes no 0.3
diagnostics/face-connectivity/fix-free-faces face-zones *() stitch 0.2 3
diagnostics/quality/general-improve face-zones *() skewness 0.7 30 10 yes
diagnostics/quality/smooth face-zones *() 10 yes
diagnostics/quality/collapse face-zones *() skewness 0.7 30 20 yes
diagnostics/quality/delaunay-swap face-zones *() skewness 0.7 30 10 yes
diagnostics/face-connectivity/fix-slivers face-zones *() 0 0.82
diagnostics/face-connectivity/fix-slivers face-zones *() 0 0.8
""" % (file_path, scdoc_file)
    return message


def boundary_rename():
    internal = ['evap_in', 'evap_out', 'heater_in', 'heater_out']
    message = ""
    for i in face_list:
        # message += r"boundary/manage/name *%s* %s" % (i, i)
        if "inlet" in i:
            message += "boundary/manage/type %s() mass-flow-inlet\n" % i
        if i in internal:
            message += "boundary/manage/type %s() internal\n" % i
        if "outlet" in i:
            message += "boundary/manage/type %s() outlet-vent" % i
    return message


def size():
    message = """
size-functions/set-global-controls 0.001 0.015 1.25
size-functions/create curvature edge *() edge-curvature 0.001 0.005 1.25 18 
size-functions/create curvature face *() face-curvature 0.001 0.005 1.25 18
size-functions/create proximity face *() face-proximity 0.001 0.005 1.25 3 face-face no yes
size-functions/create proximity edge *() edge-proximity 0.001 0.005 1.25 3 
size-functions/set-prox-gap-tolerance 0.0001
"""
    return message


def chang_type():
    message = """
objects/volumetric-regions/compute *() no yes
objects/volumetric-regions/change-type * *() fluid
"""
    for i in face_list:
        if "door" in i:
            message += "objects/volumetric-regions/change-type * %s() dead" % i
    return message


def auto_mesh():
    message = """
mesh/tet/controls/cell-sizing geometric 1.33
mesh/auto-mesh *() no pyramids tet yes
mesh/modify/auto-node-move *() *() 0.78 50 120 yes 15
"""
    return message


def body_rename():
    message = ""
    for i in volume_list:
        message = "mesh/manage/name *%s* %s\n" % (i, i)
    return message


def read_solve_jou(file_path, file_name):
    message = "file/write-mesh %s/%s.msh" % (file_path, file_name)
    if "temp" in face_list:
        message += "file/read-journal %s/%s_rotate.jou" % (file_path, file_name)
    message += r"""
switch-to-solution-mode yes
file/read-journal %s\%s_solve.jou
""" % (file_path, file_name)
    return message


def write_mesh_jou(file_path, file_name):
    new_mesh_jou = file_name + "_mesh.jou"
    scdoc_file = file_name + ".scdoc"
    message = ""
    message += import_scdoc(file_path, scdoc_file)
    message += boundary_rename()
    message += size()
    message += chang_type()
    message += auto_mesh()
    message += body_rename()
    message += read_solve_jou(file_path, file_name)
    os.chdir(file_path)
    fp = open(new_mesh_jou, 'w')
    fp.write(message)
    fp.close()
    print("%s 写入成功" % new_mesh_jou)
    # os.system(new_mesh_jou)


def import_mesh(outlet_loos_coef, massflowin):
    message = """
file/set-tui-version "19.1"
define/models/viscous/ke-standard yes
"""
    if "v_heater" in volume_list:
        message += "define/models/energy yes no no no yes q q "
    message += "solve/set/p-v-coupling 24\nsolve/set/pseudo-transient yes yes 1 1 0 "
    if "v_heater" in volume_list:
        message += "yes 3"
    message += """
solve/set/warped-face-gradient-correction/enable yes no
solve/monitors/residual/criterion-type 3 
;define/boundary-conditions/zone-type  *-shadow() interior
define/boundary-conditions/zone-type  inlet mass-flow-inlet
define/boundary-conditions/zone-type  outlet* () outlet-vent
define/boundary-conditions/set/outlet-vent *() loss-coefficient constant %s 
ke-spec no yes turb-intensity 5 turb-length-scale 0.05 q
define/boundary-conditions/set/mass-flow-inlet inlet() mass-flow no %s q
""" % (outlet_loos_coef, massflowin)
    return message


def htr_temp(heater_temp):
    message = ""
    if "v_heater" in volume_list:
        message = """
define/boundary-conditions/zone-type heater_*() radiator
define/units temperature c
define/boundary-conditions/set/mass-flow-inlet inlet() t0 no 0 q
define/boundary-conditions/set/radiator heater_in heater_out() temperature %s hc constant 1e7 q
""" % heater_temp
    return message


def core(evap_C1, evap_C2, evap_dx1, evap_dx2, evap_dy1, evap_dy2, evap_dz1, evap_dz2,
         heater_C1, heater_C2, heater_dx1, heater_dx2, heater_dy1, heater_dy2, heater_dz1, heater_dz2):
    p = []
    message = ""
    for i in volume_list:
        if "evap" in i:
            p = ["v_evap", evap_dx1, evap_dy1, evap_dz1, evap_dx2, evap_dy2, evap_dz2, evap_C1, evap_C2, ""]
        if "heater" in i:
            p = ["v_heater", heater_dx1, heater_dy1, heater_dz1, heater_dx2, heater_dy2, heater_dz2,
                 heater_C1, heater_C2, "yes no"]

        message = """
define/boundary-conditions/fluid %s no no no no no 0 no 0 no 0 no 0 no 1 no 0 no no no 
yes no no %s no %s no %s no %s no %s no %s 
yes no %s no 1e10 no 1e10 yes no %s no 1e5 no 1e5 0 0 no 1 constant 1 %s no
""" % (p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])
    return message


def solve(file_path, file_name, iterate_num):
    message = ""
    if "v_evap" in volume_list:
        message += """
solve/report-definitions/add/pressure surface-areaavg field pressure 
per-surface yes surface-names evap_*() average-over 1 q 
solve/report-plots/add/pressure report-defs pressure() print yes q
"""
    message += """
solve/report-definitions/add/velocity surface-areaavg field velocity-magnitude 
per-surface yes surface-names outlet_*() average-over 1 q 
solve/report-plots/add/velocity report-defs velocity() print yes q

solve/set/poor-mesh-numerics/cell-quality-based? yes set-quality-threshold 0.1 print-poor-elements-count
solve/initialize/hyb-initialization yes
solve/iterate %s
file/write-case-data %s/%s.cas ok
""" % (iterate_num, file_path, file_name)
    return message


def write_solve_jou(file_path, file_name, outlet_loos_coef, massflowin, heater_temp, iterate_num,
                    evap_C1, evap_C2, evap_dx1, evap_dx2, evap_dy1, evap_dy2, evap_dz1, evap_dz2,
                    heater_C1, heater_C2, heater_dx1, heater_dx2, heater_dy1, heater_dy2, heater_dz1, heater_dz2):
    new_solve_jou = file_name + "_solve.jou"
    message = ""
    message += import_mesh(outlet_loos_coef, massflowin)
    message += htr_temp(heater_temp)
    message += core(evap_C1, evap_C2, evap_dx1, evap_dx2, evap_dy1, evap_dy2, evap_dz1, evap_dz2,
                    heater_C1, heater_C2, heater_dx1, heater_dx2, heater_dy1, heater_dy2, heater_dz1, heater_dz2)
    message += solve(file_path, file_name, iterate_num)
    message += report_data(file_path, file_name)
    os.chdir(file_path)
    fp = open(new_solve_jou, 'w')
    fp.write(message)
    fp.close()
    print("%s 写入成功" % new_solve_jou)
    # os.system(new_solve_jou)


def report_data(file_path, file_name):
    message = ""
    face = ""
    if "v_evap" in volume_list:
        face += "evap_* "
    if "v_heater" in volume_list:
        face += "heater_* "
    face += "outlet_* "
    part = ["total-pressure", "static_pressure", "velocity"]
    for i in part:
        message += """
report/surface-integrals/area-weighted-avg 
inlet %s() %s yes 
%s/%s.txt yes
""" % (face, i, file_path, i)

    if "v_heater" in volume_list:
        message += """
report/surface-integrals/area-weighted-avg inlet outlet_* () temperature yes
{file_path}/temperature.txt yes
display/open-window 7
display/objects/create pathlines pathlines_inlet_t field temperature 
color-map format %0.1f size 10 q step 2000 skip 2 surfaces-list inlet() q
display/objects/display pathlines_inlet_t
display/views/restore-view isometric q
display/views/auto-scale
display/set/picture/driver/avz
display/save-picture {file_path}/pathlines_inlet_t.avz ok
""".format(file_path=file_path)

    message += """
report/surface-integrals/uniformity-index-area-weighted
inlet {face}() velocity yes 
{file_path}/uniformity.txt yes

report/surface-integrals/volume-flow-rate inlet outlet_* () yes 
{file_path}/volume_flow.txt yes

display/open-window 5
display/set/overlays yes
display/set/mesh-display-configuration/post-processing
display/mesh-outline
;display/objects/delete pathlines_inlet_v
display/objects/create pathlines pathlines_inlet_v field velocity-magnitude 
color-map format %0.1f size 10 q step 2000 skip 2 surfaces-list inlet() q
display/objects/display pathlines_inlet_v
display/views/restore-view isometric q
display/views/auto-scale
display/set/picture/driver/avz
display/save-picture {file_path}/pathlins_inlet_v.avz ok

display/open-window 6
display/objects/create pathlines pathlines_inlet_p field pressure 
color-map format %0.1f size 10 q step 2000 skip 2 surfaces-list inlet() q
display/objects/display pathlines_inlet_p
display/views/restore-view isometric q
display/views/auto-scale
display/set/picture/driver/avz
display/save-picture {file_path}/pathlins_inlet_p.avz ok

display/open-window 10
display/set/lights/lights-on yes
display/set/lights/headlight-on yes
views/camera/projection orthographic
display/set/colors/color-by-type no
display/set/filled-mesh yes
display/set/rendering-options/surface-edge-visibility no
display/set/mesh-display-configuration/meshing 
display/mesh-outline
display/views/restore-view isometric q
display/set/picture/driver/avz
display/save-picture save_path/model.avz
display/set/lights/lights-on no
display/set/lights/headlight-on no
display/set/colors/color-by-type yes
display/set/filled-mesh no
display/set/rendering-options/surface-edge-visibility yes yes
display/mesh-outline

file/write-case-data {file_path}/{file_name} ok
exit yes
""".format(face=face, file_path=file_path, file_name=file_name)
    return message
