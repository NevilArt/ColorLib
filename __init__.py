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

import bpy

from bpy.props import CollectionProperty, IntProperty

from .operators import register_operator, unregister_operator
from .data import update_file_list, update_category_list
from .panel import register_panel, unregister_panel, ColorLibItem


def register():
	register_operator()
	register_panel()

	Scene = bpy.types.Scene

	Scene.color_pallete_file_list = CollectionProperty(type=ColorLibItem)
	Scene.color_pallete_file_list_index = IntProperty(update=update_file_list)

	Scene.color_pallete_category_list = CollectionProperty(type=ColorLibItem)
	Scene.color_pallete_category_list_index = IntProperty(
		update=update_category_list
	)


def unregister():
	unregister_panel()
	unregister_operator()

	
	Scene = bpy.types.Scene

	del Scene.color_pallete_file_list
	del Scene.color_pallete_file_list_index

	del Scene.color_pallete_category_list
	del Scene.color_pallete_category_list_index


if __name__ == '__main__':
	register()