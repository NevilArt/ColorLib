############################################################################
#	This program is free software, you can redistribute it and/or modify
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
#	along with this program.  If not, see <https,//www.gnu.org/licenses/>.
############################################################################
import os
import json

from bpy.utils import previews


def get_folder_path():
	return os.path.join(os.path.dirname(__file__), 'json')


def get_value(data, key):
	return data[key] if key in data else None


def get_color(data):
	if 'color' in data:
		return data['color']
	if 'base color' in data:
		return data['base color']
	return (0.0, 0.0, 0.0, 1.0)


def get_file_name_list():
	folder_path = get_folder_path()

	if not os.path.exists(folder_path):
		return []
	
	files = sorted(os.listdir(folder_path))
	names = []

	for file in files:
		if os.path.isfile(os.path.join(folder_path, file)):
			file_name, _ = os.path.splitext(file)
			names.append(file_name)

	return names


def load_json_data_from_file(name):
	file_name = get_folder_path() + os.sep + name + ".json"
	with open(file_name, 'r') as file:
		data = json.load(file)
	return data


def get_icon(cls):
	global FILE_DATA

	rgb = cls.color if cls.color else (0.0, 0.0, 0.0, 1.0)
	color = [rgb[0], rgb[1], rgb[2], rgb[3]]

	pixels = [*color] * 1024
	icon = FILE_DATA.preview.new(cls.caption)
	icon.icon_size = (32, 32)
	icon.is_icon_custom = True
	icon.icon_pixels_float = pixels
	return icon


class Color_Data:
	def __init__(self, caption, data):
		# Main Parameters
		self.caption = caption # ""
		self.color = get_color(data) #(0.0, 0.0, 0.0, 1.0)
		self.icon = get_icon(self)

		# Optinal Parameters
		self.type = get_value(data, 'type') # ""
		self.alpha = get_value(data, 'alpha') # 1.0
		self.absorption_color = get_value(data, 'absorption_color') # (0.0, 0.0, 0.0, 1.0)
		self.anisotropic = get_value(data, 'anisotropic') # 0.0
		self.anisotropic_rotation = get_value(data, 'anisotropic_rotation') # 0.0
		self.blackbody_intensity = get_value(data, 'blackbody_intensity') # 0.0
		self.blackbody_tint = get_value(data, 'blackbody_tint') # 0.0
		self.clear_coat = get_value(data, 'clear_coat') # 0.0
		self.clear_coat_roughness = get_value(data, 'clear_coat_roughness') # 0.0
		self.clear_coat_normal = get_value(data, 'clear_coat_normal') # (0.0, 0.0, 0.0)
		self.coat_weight = get_value(data, 'coat_weight') # 0.0
		self.coat_roughness = get_value(data, 'coat_roughness') # 0.02
		self.coat_ior = get_value(data, 'coat_ior') # 1.5
		self.coat_tint = get_value(data, 'coat_tint') # (1.0, 1.0, 1.0, 1.0)
		self.coat_normal = get_value(data, 'coat_normal') # (0.0, 0.0, 0.0)
		self.color_attribute = get_value(data, 'color_attribute') # ""
		self.density = get_value(data, 'density') # 1.0
		self.density_attribute = get_value(data, 'density_attribute') # ""
		self.diffuse_roughness = get_value(data, 'diffuse_roughness') # 0.0
		self.distribution = get_value(data, 'distribution') # ""
		self.distribution = get_value(data, 'distribution') # ""
		self.edge_tint = get_value(data, 'edge_tint') # (0.0, 0.0, 0.0, 1.0)
		self.emission_color = get_value(data, 'emission_color') # (1.0, 1.0, 1.0, 1.0)
		self.emission_strength = get_value(data, 'emission_strength') # 0.0
		self.extinction = get_value(data, 'extinction') # (3.9, 3.4, 3.0)
		self.falloff = get_value(data, "falloff") # ""
		self.fresnel_type = get_value(data, 'fresnel_type') # ""
		self.ior = get_value(data, 'ior') # 1.5
		self.metallic = get_value(data, 'metallic') # 0.0
		self.normal = get_value(data, 'normal') # (0.0, 0.0, 0.0)
		self.radius = get_value(data, 'radius') # (1.0, 0.2, 0.1)
		self.roughness = get_value(data, 'roughness') # 0.5
		self.rotation = get_value(data, 'rotation') # 0.0
		self.scale = get_value(data, 'scale') # 0.05
		self.sheen = get_value(data, 'sheen') # 0.0
		self.sheen_weight = get_value(data, 'sheen_weight') # 0.0
		self.sheen_roughness = get_value(data, 'sheen_roughness') # 0.5
		self.sheen_tint = get_value(data, 'sheen_tint') # (1.0, 1.0, 1.0, 1.0)
		self.specular = get_value(data, 'specular') # (0.03, 0.03, 0.03, 1.0)
		self.specular_ior_level = get_value(data, 'specular_ior_level') # 0.5
		self.specular_tint = get_value(data, 'specular_tint') # (1.0, 1.0, 1.0, 1.0)
		self.strength = get_value(data, 'strength') # 1.0
		self.subsurface_anisotropy = get_value(data, 'subsurface_anisotropy') # 0.0
		self.subsurface_ior = get_value(data, 'subsurface_ior')
		self.subsurface_method = get_value(data, 'subsurface_method') # ""
		self.subsurface_radius = get_value(data, 'subsurface_radius') # (1.0, 0.2, 0.1)
		self.subsurface_scale = get_value(data, 'subsurface_scale') # 0.05
		self.subsurface_weight = get_value(data, 'subsurface_weight') # 0.0
		self.tangent = get_value(data, 'tangent') # (0.0, 0.0, 0.0)
		self.temperature = get_value(data, 'temperature') # 1000.0
		self.temperature_attribute = get_value(data, 'temperature_attribute') # ""
		self.thin_film_thickness = get_value(data, 'thin_film_thickness') # 0.0
		self.thin_film_ior = get_value(data, 'thin_film_ior') # 1.3
		self.transmission = get_value(data, 'transmission') # 0.0
		self.transmission_weight = get_value(data, 'transmission_weight') # 0.0
		self.transparency = get_value(data, 'transparency') # 0.0


class Category_Data:
	def __init__(self, owner):
		self.owner = owner
		self.data = []
		self.index = -1
		self.caption = ""
		self.message = ""

	def get_data(self, ctx):
		scene = ctx.scene
		new_index = scene.color_pallete_category_list_index

		# avoid recalculate is index not changed
		if new_index == self.index:
			return self.data
		
		category_key = scene.color_pallete_category_list[
			scene.color_pallete_category_list_index
		].name
		data = self.owner.data[category_key]

		self.data.clear()
		self.owner.preview.clear()

		for key in data.keys():
			color_data = data[key]
			self.data.append(Color_Data(key, color_data))

		return self.data
	
	def get_names(self, ctx):
		scene = ctx.scene
		scene.color_pallete_category_list.clear()

		names = self.owner.data.keys()

		for name in names:
			item = scene.color_pallete_category_list.add()
			item.name = name
	
	def get_color(self, index):
		# TODO add out of range check 
		return self.data[index]

	def reset(self):
		self.index = -1


class File_Data:
	def __init__(self):
		self.names = []
		self.data = {}
		self.index = -1
		self.subdata = Category_Data(self)
		self.preview = previews.new()

	def get_names(self, ctx):
		scene = ctx.scene
		scene.color_pallete_file_list.clear()

		if not self.names:
			self.names = get_file_name_list()

		for name in self.names:
			item = scene.color_pallete_file_list.add()
			item.name = name

	def get_data(self, ctx):
		scene = ctx.scene
		new_index = scene.color_pallete_file_list_index

		# avoid recalculate is index not changed
		if new_index == self.index:
			return self.data
		
		name = scene.color_pallete_file_list[new_index].name
		self.data = load_json_data_from_file(name)
		self.index = new_index

		return self.data

	def reset(self):
		self.index = -1
		self.preview.clear()
		self.subdata.reset()


FILE_DATA = File_Data()


# TODO chose better name
def update_file_list(cls, ctx):
	global FILE_DATA
	FILE_DATA.get_data(ctx)
	FILE_DATA.subdata.get_names(ctx)


# TODO chose better name
def update_category_list(cls, ctx):
	global FILE_DATA
	Category = FILE_DATA.subdata
	data = Category.get_data(ctx)


def get_file_data():
	global FILE_DATA
	return FILE_DATA