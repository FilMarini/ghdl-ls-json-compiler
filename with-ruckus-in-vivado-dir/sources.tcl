########################################################
## Get variables and Custom Procedures
########################################################
source -quiet $::env(RUCKUS_DIR)/vivado/env_var.tcl
source -quiet $::env(RUCKUS_DIR)/vivado/proc.tcl

# Source hdl-prj.json generator
#SourceTclFile ${VIVADO_DIR}/ghdl-proj-gen.tcl
#ghdl-ls-prj-gen ${TOP_DIR}

SourceTclFile ${VIVADO_DIR}/vhdlmode-prj-gen.tcl
vhdlmode-prj-gen ${TOP_DIR} RUDP