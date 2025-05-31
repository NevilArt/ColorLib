############################################################################
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.
############################################################################

import os

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from bpy.props import BoolProperty, IntProperty

from .color import rgba_to_hex
from .material import create_material
from .data import get_file_data


class ColorLib_OT_Refresh_File_List(Operator):
	bl_idname = 'color_pallete.refresh'
	bl_label = "Refresh Color pallete List"
	bl_options = {'REGISTER', 'INTERNAL'}

	def execute(self, ctx):
		get_file_data().names.clear() # active only on development mode
		get_file_data().get_names(ctx)
		return {'FINISHED'}


#TODO change to name material greator or seprate to two operators
class ColorLib_OT_Actor(Operator):
	bl_idname = 'color_pallete.actor'
	bl_label = "Color Pallete Actor"
	bl_description = ""
	bl_options = {'REGISTER', 'INTERNAL'}

	index: IntProperty() # type: ignore
	create_pbr: BoolProperty(default = False) # type: ignore

	def execute(self, ctx):
		if not ctx.object:
			return
		subdata = get_file_data().subdata
		color = subdata.get_color(self.index)

		if self.create_pbr:
			create_material(ctx, color.caption, color)
			subdata.message = color.caption + " Shader Created" 

		else:
			hex = rgba_to_hex(color.color)
			ctx.window_manager.clipboard = hex
			subdata.message = "Clipboard : " + hex

		return {'FINISHED'}


classes = {
	ColorLib_OT_Refresh_File_List,
	ColorLib_OT_Actor
}

def register_operator():
	for cls in classes:
		register_class(cls)


def unregister_operator():
	for cls in reversed(classes):
		unregister_class(cls)
