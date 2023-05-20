---
title: 'PDMaterialPoints.jl'
date: 2022-11-10
modified: 2023-05-15
authors: "Ravinder Bhattoo"
permalink: /posts/pdmaterialpoints
excerpt: "![pdmaterialpoints](/images/blogs/pdmaterialpoints/pdmaterialpoints.png) PDMaterialPoints.jl is a Julia package that can be used to generate particle-based objects for peridynamics simulations. Peridynamics is a relatively new computational framework for simulating the behavior of materials that takes into account long-range interactions between particles or points in a material, instead of the traditional continuum-based approach. PDMaterialPoints.jl can be used to create particle-based objects, such as 2D and 3D meshes, that can be used as input for peridynamics simulations."
category:
  - SciML
tags:
  - simulation
  - PDMaterialPoints.jl
mainpdmaterialpoints: true
---

[Documentation](https://ravinderbhattoo.github.io/PDMaterialPoints.jl)

PDMaterialPoints.jl is a Julia package that can be used to generate particle-based objects for peridynamics simulations. Peridynamics is a relatively new computational framework for simulating the behavior of materials that takes into account long-range interactions between particles or points in a material, instead of the traditional continuum-based approach. PDMaterialPoints.jl can be used to create particle-based objects, such as 2D and 3D meshes, that can be used as input for peridynamics simulations.

![pdmaterialpoints](/images/blogs/pdmaterialpoints/pdmaterialpoints.png)

In this article, we will provide an overview of the types and methods available in the PDMaterialPoints.jl package.

## Types

PDMaterialPoints.jl provides several types for creating different shapes of particle-based objects:

- `Cone`: A type representing a cone-shaped object with a given radius and length.
- `Cuboid`: A type representing a cuboid-shaped object with given minimum and maximum bounds.
- `Cylinder`: A type representing a cylinder-shaped object with a given radius, wall thickness, and length.
- `Disk`: A type representing a disk-shaped object with a given radius and thickness.
- `PostOpObj`: A type representing a post-operation object that is created lazily from another object and an operation to be applied.
- `Shape`: An abstract type representing a generic shape object.
- `Sphere`: A type representing a sphere-shaped object with a given radius.

## Methods

PDMaterialPoints.jl provides several methods for creating, manipulating, and deleting particle-based objects:

- `create`: An abstract method for creating a mesh object of a given shape with optional resolution, random perturbation, and particle type.
- `changetype`: A method for changing the particle type of a mesh object using a boolean array generated from a given function.
- `delete`: A method for deleting mesh particles of a mesh object using a boolean array generated from a given function.
- `move`: A method for moving mesh particles of a mesh object by a given displacement.
- `rotate`: A method for rotating a shape object by a given angle about a given vector and point.
- `velocity`: A method for changing the velocity of mesh particles of a mesh object using a boolean array generated from a given function and a given velocity.

The `create` method is an abstract method that generates a mesh object of a given shape. It can take optional parameters such as resolution, random perturbation, and particle type. The resolution parameter controls the number of particles in the mesh object. The random perturbation parameter can be used to introduce random noise into the mesh object, which can be useful for simulating realistic materials. The particle type parameter specifies the type of particle to use in the mesh object, which can be useful for simulating different types of materials.

The `changetype` method is used to change the type of particle in a mesh object. It takes a boolean array generated from a given function as input, which specifies the particles to be changed. The `delete` method is used to delete particles from a mesh object. It also takes a boolean array generated from a given function as input, which specifies the particles to be deleted.

The `move` method is used to move particles in a mesh object by a given displacement. It takes a mesh object and a displacement vector as input, and moves the particles in the mesh object by the given displacement vector. The `rotate` method is used to rotate a shape object by a given angle about a given vector and point. It takes a shape object, an angle, a vector, and a point as input, and rotates the shape object by the given angle about the given vector and point.

The `velocity` method is used to change the velocity of particles in a mesh object. It takes a boolean array generated from a given function as input, which specifies the particles to be changed.

Finally, the `delete` method enables users to delete particles from an object using a boolean array from a specified function.

## Examples (see [documentation](https://ravinderbhattoo.github.io/PDMaterialPoints.jl) for more examples)

Creating a mesh for a composite material using PDMaterialPoints can be done by combining different shapes together. Here are some examples of composite material meshes that can be created using PDMaterialPoints:

1. Composite material with randomly placed inclusions

```julia
println("Creating a composite...")

using PDMaterialPoints

function rand_(a, b)
    return a + rand()*(b-a)
end

obj = Cuboid([-10 10; -10 10; 0 3])
for i in 1:100
    global obj
    center = [rand_(-10, 10), rand_(-10, 10), rand_(0, 3)]
    radius = 0.2 + 1.0*rand()
    obj = changetype(obj, out -> begin x=out[:x]; mask = sum((x .- vec(center)).^2, dims=1) .< radius^2; mask .& (sum(out[:type][mask[1,:]] .== 2) == 0)  end, 2)
end

out = create(obj, resolution=0.1, rand_=0.0, type=1)
write_data("./output/composite.data", out)
```

![composite_block](/images/blogs/pdmaterialpoints/composite_block.png)

2. Rotating composite strip

```julia
println("Creating rotating strip...")

using PDMaterialPoints

c = Cuboid([-5 5; -10 10; 0 3])
obj = copy(c)

for i in 1:100
    global obj
    obj = changetype(obj, out -> begin x=out[:x]; sum(x[1:2, :].^2, dims=1) .< 3.0^2 end, 2)
    obj = changetype(obj, out -> begin x=out[:x]; sum(x[1:2, :].^2, dims=1) .< 2.0^2 end, 3)
    obj = move(obj, by=[10.0, 0.0, 0.0])
    obj = rotate(obj, angle=2, point=[0.0, 0.0, 0.0], vector_=[1.0, 1.0, 0.0])
    obj = combine(obj, c)
end

out = create(obj, resolution=0.5, rand_=0.0, type=1)
write_data("./output/strip.data", out)
```

![composite_strip](/images/blogs/pdmaterialpoints/composite_strip.png)


The output files generated by PDMaterialPoints.jl can be visualized using third-party software such as Ovito. PDMaterialPoints.jl is a useful tool for researchers and scientists who are interested in studying the behavior of particles in various settings, such as materials science, fluid dynamics, and more.

The examples provided show how PDMaterialPoints.jl can be used to create a range of particle configurations, from simple shapes such as spheres and cylinders to complex composite structures. The package also supports more advanced features such as rotation and movement of particles, which can be used to model dynamic systems.

In conclusion, the PDMaterialPoints.jl package provides a set of powerful tools for generating particle-based objects for peridynamics simulations. Its various types and methods allow users to create a wide range of objects and manipulate them in various ways. Overall, the PDMaterialPoints.jl package is a useful resource for researchers and engineers working in peridynamics and related fields.