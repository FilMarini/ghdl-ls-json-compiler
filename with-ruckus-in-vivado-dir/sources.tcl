########################################################
## Get variables and Custom Procedures
########################################################
source -quiet $::env(RUCKUS_DIR)/vivado/env_var.tcl
source -quiet $::env(RUCKUS_DIR)/vivado/proc.tcl

# Source hdl-prj.json generator
SourceTclFile ${VIVADO_DIR}/ghdl-proj-gen.tcl
ghdl-ls-prj-gen ${TOP_DIR}/.. -include_path /home/fmarini/.vivado_libs/ghdl/Vivado_2021.1/comp/08/

SourceTclFile ${VIVADO_DIR}/vhdlmode-prj-gen.tcl
#vhdlmode-prj-gen ${TOP_DIR}/.. ${VIVADO_PROJECT} False
