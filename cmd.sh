# Use shell file, more convenient to set env vars etc... compared to makefile.
# Meant to be sourced into bash

export NOEL_RW_SCRIPTS_ROOT="$HOME/projects/risingwave-dev-scripts"

# Run wide table stuff
function wide-table() {
  "${NOEL_RW_SCRIPTS_ROOT}/wide_table.py" "$@"
}

function refresh() {
  source "${NOEL_RW_SCRIPTS_ROOT}/cmd.sh"
}

function srw() {
  ./risedev d full
}

function heaprw() {
  RISEDEV_ENABLE_HEAP_PROFILE=true ./risedev d full
}