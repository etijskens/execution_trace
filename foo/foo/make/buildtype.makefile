#===============================================================================
# et/make/buildtype.makefile
#
# Set the build type, and some pretty standard CFLAGS
#
# Input variables:
#   . $(build) : "Release"[*], "Debug". If build is set on the command line to
# 	  		"release" or "debug", it is converted to "Release", resp. "Debug"
#   . $(NO_ERROR) : suppress error when $(build) contains another build
#			configuration than Release or Debug.
# Output variables:
#   . PROJECT_BUILD := $(PROJECT_ROOT)/build/$(build_type)
#   . WORKSPACE := $(ET)/..
#===============================================================================

include $(MAKE_INCLUDE)/msg.makefile

ifeq ($(verbose),1)
$(info ) # print emtpy line
$(call ENTER)
endif

WORKSPACE := $(abspath $(ET)/..)

ifndef TOOLCHAIN
$(call WARNING,toolchain.makefile was not included before buildtype.makefile!)
else
ifeq ($(verbose),1)
$(call INFO, ICPC ='$(ICPC)')
$(call INFO, IFORT='$(IFORT)')
$(call INFO, ICC  ='$(ICC)')
endif
endif

ifndef build
build_type := Release
else
build_type := $(build)
endif
# Ensure that "make build=debug" and "make build=Debug" have the same effect,
# as well as  "make build=release" and "make build=Release".
ifeq ($(build),debug)
override build_type := Debug
else ifeq ($(build),release)
override build_type := Release
endif

PROJECT_BUILD := $(PROJECT_ROOT)build/$(build_type)

#-------------------------------------------------------------------------------
# compiler flags
ifeq ($(IFORT),1)
AVX_FLAG := -march=core-avx2
else
AVX_FLAG := -mavx2
endif

ifeq ($(verbose),1)
$(call INFO, AVX_FLAG=$(AVX_FLAG))
endif

ifeq ($(build_type),Debug)
CFLAGS   += -g -O0 -Wall -DDEBUG
F90FLAGS += $(CFLAGS)

else ifeq ($(build_type),Release)
CFLAGS   += -g -O2 $(AVX_FLAG)
F90FLAGS += $(CFLAGS)

else ifndef NO_ERROR
# do not indent $(error msg)!
$(info  ERROR: Build mode $(build) not supported by this Makefile)
$(error ERROR ***)
endif

$(call INFO,"Build type    = $(build_type)")
$(call INFO,"PROJECT_BUILD = $(PROJECT_BUILD)")
ifeq ($(verbose),1)
$(call LEAVE)
$(info ) # print emtpy line
endif
