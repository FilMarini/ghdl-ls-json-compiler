all: hdl-prj-gen vhdl-mode-prj

hdl-prj-gen:
	pip install ./hdl_prj_gen

vhdl-mode-prj:
	pip install ./vhdl_mode_prj_gen

clean:
	rm $(HOME)/.local/bin/hdl-prj-gen
	rm $(HOME)/.local/bin/vhdl-mode-prj-gen
