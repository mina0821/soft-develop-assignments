JFLAGS = -g
#JCLASS = -cp $(CLASSPATH):src:/usr/share/java/junit.jar
JCLASS = -cp $(CLASSPATH):src:/usr/share/java/junit4.jar # on mills
JC = javac
JVM = java
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = doxConfig
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $(JCLASS) $*.java

CLASSES = \
	src/Constants.java \
	src/Obstacles.java \
	src/Destinations.java \
	src/PathCalculation.java \
	src/FullSequenceException.java \
	src/PathT.java \
	src/GenericList.java \
	src/PointT.java \
	src/InvalidPointException.java \
	src/InvalidPositionException.java \
	src/RegionT.java \
	src/InvalidRegionException.java \
	src/SafeZone.java \
	src/Map.java \
	src/TestPathCalculation.java \
	src/AllTests.java

MAIN = src/AllTests

default: classes

classes: $(CLASSES:.java=.class)

test: $(MAIN).class
	$(JVM) $(JCLASS) org.junit.runner.JUnitCore AllTests

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

clean:
	$(RM) *.class
