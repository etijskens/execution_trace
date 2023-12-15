// read macosx_issue.txt before trying this on mac os x mojave!

#include <boost/python.hpp>
using namespace boost::python;

#include <numpy_boost_python.hpp>
#include <iostream>
#include <assert.h>

void
sum
  ( numpy_boost<double,1> a
  , numpy_boost<double,1> b
  , numpy_boost<double,1> c
  )
{// compute c = a+b
	std::cout <<"hello"<<std::endl;
	size_t na = static_cast<size_t>(a.shape()[0]);
	size_t nb = static_cast<size_t>(b.shape()[0]);
	size_t nc = static_cast<size_t>(c.shape()[0]);
	assert (na==nb);
	assert (na==nc);
	std::cout<<"na="<<na<<std::endl;

	double* const pa = a.origin();
	double* const pb = b.origin();
	double*       pc = c.origin();
	for( size_t i=0; i<na; ++i) {
		pc[i] = pa[i]+pb[i];
	}
}

BOOST_PYTHON_MODULE(bar_cpp)
{
 // Initialize the Numpy support
    IMPORT_ARRAY();

 // You must call this function inside of the BOOST_PYTHON_MODULE
 // init function to set up the type conversions.  It must be called
 // for every type and dimensionality of array you intend to return.
 // If you don't, the code will compile, but you will get error
 // messages at runtime.
 // numpy_boost_python_register_type<int   ,1>();
    numpy_boost_python_register_type<double,1>();
 // numpy_boost_python_register_type<double,2>();
 // numpy_boost_python_register_type<float ,1>();

 // Exported functions:
    def("sum",sum);
}
