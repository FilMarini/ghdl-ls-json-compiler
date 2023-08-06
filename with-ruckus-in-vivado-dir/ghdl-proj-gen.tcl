proc ghdl-ls-prj-gen {out_path} {
    # Check if VHDL 2008 is used in project
    set vhdl_2008 0
    if {[lsearch -exact [get_property FILE_TYPE [get_files -used_in synthesis -compile_order sources]] {VHDL 2008}] >= 0} {
        set vhdl_2008 1
    }
    if {[lsearch -exact [get_property FILE_TYPE [get_files -used_in simulation -compile_order sources]] {VHDL 2008}] >= 0} {
        set vhdl_2008 1
    }

    # Set GHDL analyze options to JSON file
    set ghdl_opt "\{\n"
    set ghdl_opt "${ghdl_opt}\t\"options\": \{\n"
    set ghdl_opt "${ghdl_opt}\t\t\"ghdl_analysis\": \[\n"
    if {$vhdl_2008 == 1} {
        set ghdl_opt "${ghdl_opt}\t\t\t\"--std=08\",\n"
    }
    set ghdl_opt "${ghdl_opt}\t\t\t\"--ieee=synopsys\",\n"
    set ghdl_opt "${ghdl_opt}\t\t\t\"-fexplicit\"\n"
    set ghdl_opt "${ghdl_opt}\t\t\]\n"
    set ghdl_opt "${ghdl_opt}\t\},\n"

    # Get set of files used in synthesis
    set synth_list [get_files -compile_order sources -used_in synthesis]
    # Get set of files used in simulation
    set sim_list [get_files -compile_order sources -used_in simulation]
    # And merge them
    foreach el $sim_list {
        if {[lsearch -exact $synth_list $el] < 0} {
            lappend synth_list $el
        }
    }

    # Write file infos to JSON file
    set ghdl_files "${ghdl_opt}\t\"files\": \[\n"
    for { set i 0 } { $i < [llength $synth_list] } { incr i } {
        set el [lindex $synth_list $i]
        # Get Library
        set file_library [get_property LIBRARY [get_files $el]]
        # Get File type
        set file_type "unknown"
        set extension [file extension $el]
        if {[string equal $extension .vhd] || [string equal $extension .vhdl]} {
            set file_type vhdl
        } elseif {[string equal $extension .v]} {
            set file_type verilog
        } elseif {[string equal $extension .sv]} {
            set file_type systemverilog
        } elseif {[string equal $extension .dcp]} {
            set file_type dcp
        }
        # Set file info
        if {$i < [llength $synth_list] - 1} {
            set ghdl_files "${ghdl_files}\t\t\{ \"file\": \"$el\", \"library\": \"$file_library\", \"language\": \"$file_type\"\},\n"
        } else {
            set ghdl_files "${ghdl_files}\t\t\{ \"file\": \"$el\", \"library\": \"$file_library\", \"language\": \"$file_type\"\}\n"
        }
    }

    # End file
    set ghdl_files "${ghdl_files}\t\]\n"
    set ghdl_files "${ghdl_files}\}"

    # Write to JSON file
    set out_path "${out_path}/hdl-prj.json"
    set outfile [open $out_path w]
    puts $outfile $ghdl_files
    close $outfile
    return 0
}

