#-------------------------------------------------------------------------------
# Makefile project et/test_numpy_boost
#-------------------------------------------------------------------------------
# Variables in lowercase are meant to be set from the command line,
# although they usually have a default[*].
#   . build= release[*], debug, Release, Debug.

SHELL        := bash
PROJECT_ROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
BIN          := $(ET)/bin
MAKE_INCLUDE := ./make

TARGET       := foo
OBJS = $(TARGET).o


include $(MAKE_INCLUDE)/buildtype.makefile
include $(MAKE_INCLUDE)/toolchain.makefile
# Additional compiler flagsÍ
  CPPFLAGS := -std=c++17

include $(MAKE_INCLUDE)/findIntelPython.makefile

ifndef FOUND_INTEL_PYTHON
include $(MAKE_INCLUDE)/findAnacondaPython.makefile
endif

with_numpy := 1
include $(MAKE_INCLUDE)/BoostPython.makefile

# with_Vc := darwin-xcode
include $(MAKE_INCLUDE)/Vc.makefile

include $(MAKE_INCLUDE)/prefixes.makefile

.SUFFIXES: .o .cpp .so

#-------------------------------------------------------------------------------
.PHONY: all check
all: $(PROJECT_ROOT)/$(TARGET).so check

#-------------------------------------------------------------------------------
$(PROJECT_ROOT)/$(TARGET).so:	$(PROJECT_BUILD)/$(TARGET).o
	@echo
	@echo "#-------------------------------------------------------------------------------"
	@echo "# Linking Python module $(TARGET).so"
	@echo "#-------------------------------------------------------------------------------"

	cd $(PROJECT_BUILD) && \
	$(CXX) -shared -fPIC -o $(TARGET).so $(TARGET).o $(LIB_DIRS) $(LIBS)
	ln -sf $(PROJECT_BUILD)/$(TARGET).so

#-------------------------------------------------------------------------------
$(PROJECT_BUILD)/%.o: $(PROJECT_ROOT)/%.cpp $(PROJECT_ROOT)/sumvc.hpp
	@echo
	@echo "#-------------------------------------------------------------------------------"
	@echo "# Compiling  $<"
	@echo "#-------------------------------------------------------------------------------"

	mkdir -p $(PROJECT_BUILD)
	cd $(PROJECT_BUILD) && \
	$(CXX) -c -fPIC $(DEFINES) $(INCLUDE_DIRS) $(CFLAGS) $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

#-------------------------------------------------------------------------------
.PHONY: check
check: $(PROJECT_ROOT)/$(TARGET).so $(PROJECT_ROOT)/test.py $(PROJECT_ROOT)/m.py
	@echo
	@echo "#-------------------------------------------------------------------------------"
	@echo "# Running: 'Python test.py' in"
	@echo "# $(realpath $(PROJECT_ROOT))"
	@echo "#-------------------------------------------------------------------------------"
	which $(PYTHON)
	@echo
	$(PYTHON) --version
	@echo
	cd $(PROJECT_ROOT) && $(PYTHON) test.py

#-------------------------------------------------------------------------------
.PHONY: clean
clean:
	@echo
	@echo "#-------------------------------------------------------------------------------"
	@echo "# make clean:"
	@echo "#-------------------------------------------------------------------------------"

	rm -rf $(PROJECT_ROOT)/$(TARGET).so $(PROJECT_BUILD)/$(TARGET).so $(PROJECT_BUILD)/*.o
