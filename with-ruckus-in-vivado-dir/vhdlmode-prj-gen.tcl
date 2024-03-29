proc vhdlmode-prj-gen {out_path args} {
    # Get args default values
    set defaults {-project None -use_abs_path False -include_sim True}
    # Merge args
    set params [dict merge $defaults $args]
    # Extract the variables I car about
    dict update params -project project -use_abs_path use_abs_path -include_sim include_sim {}

    set prj "\(setq vhdl-project \"$project\"\)\n\n"
    set prj "${prj}\(vhdl-aput 'vhdl-project-alist vhdl-project\n"
    set prj "${prj}\'\(\"Individual source files, multiple compilers in different directories\" \"[file normalize ${out_path}]/\"\n"
    set prj "${prj} \(\n"

    # Get set of files used in synthesis
    set synth_list [get_files -compile_order sources -used_in synthesis]
    if { [string equal $include_sim True] } {
        # Get set of files used in simulation
        set sim_list [get_files -compile_order sources -used_in simulation]
        # And merge them
        foreach el $sim_list {
            if {[lsearch -exact $synth_list $el] < 0} {
                lappend synth_list $el
            }
        }
    }

    foreach el $synth_list {
        # Use relative path if wanted
        if { [string equal $use_abs_path False] } {
            set el [string map "[file normalize ${out_path}] ." $el]
        }
        set prj "${prj}  \"$el\"\n"
    }

    set prj "${prj}  \)\n"
    set prj "${prj} \"\" nil \"\\\\1\/\" \"work\" \"\\\\1\/work\/\" \"Makefile\" \"\"\)\n"
    set prj "${prj}\)\n"


    # Write to JSON file
    set out_path "${out_path}/$project.prj"
    set outfile [open $out_path w]
    puts $outfile $prj
    close $outfile
    return 0
}
