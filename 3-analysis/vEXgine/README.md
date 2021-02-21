# vEXgine
[vEXgine](http://caosd.lcc.uma.es/vexgine/) is a customizable and extensible implementation of the execution engine for the [Common Variability Language (CVL)](http://caosd.lcc.uma.es/vexgine/about-cvl).  
vEXgine fully supports the materialization process to resolve the variability specified in a CVL variability model over any [MOF](https://www.omg.org/mof/)-compliant model.

We have designed the software architecture of the **Authentication**, **Encryption**, and **Hashing** FQAs in UML. We follow a negative variability approaches where we start from the complete software architecture of the FQAs and remove those architectural elements that have not been selected in a specific configuration (*resolution model*). To do that, we provide the appropriate model transformations (e.g., *ObjectExistence*) to be executed by vEXgine.
We also provide the *variability model in CVL* of the security quality attribute.

## Artifacts
* The [FQAs software architecture](appmodel.uml) in UML.
* The [FQAs variability model](SecurityFQA.xmi) of the security FQA in CVL.
* An example of [configuration (resolution model in CVL)](SecurityFQA-resolution.xmi) of the FQAs variability model.
* An example of variation point ([ObjectExistence.atl](ObjectExistenceUML.atl)) implemented as a model to model transformation in [ATL](https://www.eclipse.org/atl/) and its binary compiled version ([ObjectExistence.asm](ObjectExistenceUML.asm)).

## Procedure
Here are the instructions to manage and work with the WeaFQAs artifacts in vEXgine.
All the information about vEXgine, including documentation, downloads, and the source code is available in its [official website](http://caosd.lcc.uma.es/vexgine/).  

###### Download, install, and setup vEXgine:
1. Download the latest version of vExgine from [here](https://github.com/jmhorcas/vEXgine).  
**Note:** vEXgine requires Java JDK 8 or later.  
**Note:** You only need to download the `demo` folder in order to download the Java application of vEXgine.
2. Execute `vEXgine.jar` as a Java application (double clic or in a console type: `java -jar vExgine.jar`).
3. Edit the variability model (SecurityFQA.xmi file) with a text editor and change the filepath of the compiled model transformation (ObjectExistenceUML.asm) in line 372:    `modelTransformation="\pathto\ObjectExistenceUML.asm"`

###### Load the models and resolve the variability over the software architecure:
In vExgine:
1. Load a variability model ([SecurityFQA.xmi](SecurityFQA.xmi)).
2. Load a resolution model ([SecurityFQA-resolution.xmi](SecurityFQA-resolution.xmi)).
3. Load a base model ([appmodel.uml](appmodel.uml)).
4. (Optional) Load the metamodel of the base model (if it is different from UML).
5. Fill the base model name in the transformations (e.g., `IN`).
6. Fill the metamodel name in the transformations (e.g., `UML`).
7. Clic the central button `vExgine`. The software architecture ([appmodel.uml](appmodel.uml)) will be automatically modified according the selections made in the configuration model.

###### Advances features in vEXgine:
* To create, edit and manage CVL models and metamodels, you can use [Obeo Designer](https://www.obeodesigner.com/en/) (with the [UML Designer plugin](http://www.umldesigner.org/)).
* To use or extend the vEXgine API, you need [Maven](https://maven.apache.org/) and the libraries provided by vEXgine (located in the `lib` folder).
* To create, edit or modify ATL transformations, you can use [Eclipse Modeling Tools](https://www.eclipse.org/) (with the [ATL plugin](https://www.eclipse.org/atl/)).


## References
* [vEXgine web site](http://caosd.lcc.uma.es/vexgine/)  
* [vEXgine repository](https://github.com/jmhorcas/vEXgine)
* [CVL](http://caosd.lcc.uma.es/vexgine/about-cvl/)
* [ATL](https://www.eclipse.org/atl/)
* [MOF](https://www.omg.org/mof/)
* [Eclipse](https://www.eclipse.org/)
* [Obeo Designer](https://www.obeodesigner.com/en/)
* [UML Designer](http://www.umldesigner.org/)
* [Maven](https://maven.apache.org/)
