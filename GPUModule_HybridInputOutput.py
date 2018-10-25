##############################################################
#
#	GPUModule_HybridInoutOutput:
#	    Contains a mixin for hybrid input-output methods 
#	    within the GPUModule.Solver class.
#	
#	    Siddharth Maddali
#	    Argonne National Laboratory
#	    April 2018
#
##############################################################

class Mixin:
###########################################################################################
#   Performs <num_iterations> iterations of of hybrid input/output
###########################################################################################
    def HIO( self, num_iterations ):
        for n in list( range( num_iterations ) ):
            self.__sess__.run( self._dumpimage )
            self.__sess__.run( self._getIntermediateFFT )
            self.__sess__.run( self._modproject )
            self.__sess__.run( self._disrupt )
        return

###########################################################################################
#   Performs <num_iterations> iterations of of high-energy hybrid input/output
###########################################################################################
    def HEHIO( self, num_iterations ):
        for n in list( range( num_iterations ) ):
            self.__sess__.run( self._dumpimage )
            self.__sess__.run( self._getIntermediateFFT )
            self.__sess__.run( self._binThis )
            self.__sess__.run( self._scaleThis )
            self.__sess__.run( self._expandThis )
            self.__sess__.run( self._HEImgUpdate )
            self.__sess__.run( self._HEImgCorrect )
        return

