# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Fibonacci Lattice",
    "author": "Jan Pinter",
    "version": (3, 9),
    "blender": (2, 63, 0),
    "location": "View3D > Add > Mesh",
    "description": "Add Fibonacci lattice mesh",
    "category": "Add Mesh",
}

if "bpy" in locals():
    import importlib
    importlib.reload(FibonacciLattice)
else:
    from add_fibonacci_lattice import FibonacciLattice

import bpy

################################################################################
##### REGISTER #####

def add_fibonacci_lattice_button(self, context):
    self.layout.operator(FibonacciLattice.add_mesh_fibonacci_lattice.bl_idname, text="Fib. lattice", icon="PLUGIN")

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_mesh_add.append(add_fibonacci_lattice_button)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_mesh_add.remove(add_fibonacci_lattice_button)

if __name__ == "__main__":
    register()
