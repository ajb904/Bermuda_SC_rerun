conf: "config.yml"
SAMPLES = ["sct-8p2","sct-8p3","sct-8p4","sct-8t3","sct-8t4"]
BLANK = ["sct-bl"]

include: "rules/folder_setup.rule"
include: "rules/software_paths.rule"
include: "rules/db_download.rule"
include: "rules/read_QC.rule"
include: "rules/contaminant_filter.rule"
include: "rules/assembly_full.rule"
include: "rules/khmer.rule"
include: "rules/contig_binning.rule"

rule all:
    input:
        rules.readQC.input,
        rules.db_downloads.input,
        rules.filter_contaminants.input,
        rules.full_assemblies.input,
        rules.khmer_counting.input,
        rules.bin_contigs.input,
