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

from bpy.types import PropertyGroup, Panel, UIList
from bpy.utils import register_class, unregister_class
from bpy.props import StringProperty, FloatVectorProperty 


from .operators import ColorLib_OT_Actor
from .data import get_file_data


def draw_color_pallete(layout):
	subdata = get_file_data().subdata
	data = subdata.data

	box = layout.box()
	col = box.column(align=True)
	col.label(text=subdata.caption)

	for index, color in enumerate(data):
		raw = col.row(align=True)

		# color_box = 

		label = raw.operator(
			ColorLib_OT_Actor.bl_idname, 
			icon_value= color.icon.icon_id,
			text= color.caption,
			emboss= True
		)
		label.index = index
		label.create_pbr = False

		button = raw.operator(
			ColorLib_OT_Actor.bl_idname, 
			icon= 'MATERIAL_DATA',
			text= "",
		)
		button.index = index
		button.create_pbr = True
	
	col.label(text=subdata.message)


class COLORLIB_PT_panel(Panel):
	bl_label = "Color Library"
	bl_idname = "COLORLIB_PT_panel"
	bl_space_type = 'NODE_EDITOR'
	bl_region_type = 'UI'
	bl_category = 'ColorLib'

	@classmethod
	def poll(cls, context):
		return context.space_data.tree_type == 'ShaderNodeTree'

	def draw(self, context):
		layout = self.layout
		scene = context.scene

		box = layout.box()
		col = box.column(align=True)
		col.operator(
			'color_pallete.refresh', text="Refresh", icon='FILE_REFRESH'
		)
	
		col.template_list(
			'COLORLIB_UL_File_List', "",
			scene, 'color_pallete_file_list',
			scene, 'color_pallete_file_list_index'
		)

		col.template_list(
			'COLORLIB_UL_Categori_List', "",
			scene, 'color_pallete_category_list',
			scene, 'color_pallete_category_list_index'
		)
		
		draw_color_pallete(layout)


# Store the color pallete json file name and full address
class ColorLibItem(PropertyGroup):
	name: StringProperty(name="File Name")  # type: ignore


class ColorItem(PropertyGroup):
	color: FloatVectorProperty(
		name="Color",
		subtype='COLOR',
		size=4,
		default=(1.0, 1.0, 1.0, 1.0)
	) # type: ignore


# Display json file name with filter
class COLORLIB_UL_File_List(UIList):
	"""UI List to display files with filtering"""
	def draw_item(
			self, ctx, layout, data, item, icon,
			active_data, active_propname, index):
		
		if self.layout_type in {'DEFAULT', 'COMPACT'}:
			layout.label(text=item.name, icon='FILE')

		elif self.layout_type == 'GRID':
			layout.alignment = 'CENTER'
			layout.label(text=item.name, icon='FILE')

	def invoke(self, ctx, event):
		return {'FINISHED'}
	

# Display categories name with filter
class COLORLIB_UL_Categori_List(UIList):
	"""UI List to display files with filtering"""
	def draw_item(
			self, ctx, layout, data, item, icon,
			active_data, active_propname, index):
		
		if self.layout_type in {'DEFAULT', 'COMPACT'}:
			layout.label(text=item.name, icon='FILE')

		elif self.layout_type == 'GRID':
			layout.alignment = 'CENTER'
			layout.label(text=item.name, icon='FILE')

	def invoke(self, ctx, event):
		return {'FINISHED'}


classes = {
	COLORLIB_PT_panel,
	ColorLibItem,
	COLORLIB_UL_File_List,
	COLORLIB_UL_Categori_List
}


def register_panel():
	for cls in classes:
		register_class(cls)


def unregister_panel():
	for cls in reversed(classes):
		unregister_class(cls)