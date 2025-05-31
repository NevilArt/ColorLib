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

from .color import gamma_correction

def create_material_node(ctx, data, type, name, caption):
	node_tree = ctx.object.active_material.node_tree
	material = node_tree.nodes.new(type)
	material.name = name
	material.label = caption + " " + data.caption
	return material


def set_value(material, input_index, value):
	if value is None:
		return
	material.inputs[input_index].default_value = value


def set_color(material, input_index, color):
	if not color:
		return
	material.inputs[input_index].default_value = gamma_correction(color)


def create_metallic_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeBsdfMetallic", "Metallic BSDF", caption
	)

	if data.distribution:
		material.distribution = data.distribution
	
	if data.fresnel_type:
		material.fresnel_type = data.fresnel_type

	set_color(material, 0, data.color)
	set_color(material, 1, data.edge_tint)
	set_value(material, 2, data.ior)
	set_value(material, 3, data.extinction)
	set_value(material, 4, data.roughness)
	set_value(material, 5, data.anisotropic)
	set_value(material, 6, data.rotation)
	set_value(material, 7, data.normal)
	set_value(material, 8, data.tangent)


def create_diffuse_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeBsdfDiffuse", "Diffuse BSDF", caption
	)

	set_color(material, 0, data.color)
	set_value(material, 1, data.roughness)
	set_value(material, 2, data.normal)


def create_emssion_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeEmission", "Emission", caption
	)

	set_color(material, 0, data.color)
	set_value(material, 1, data.strength)


def create_glass_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeBsdfGlass", "Glass BSDF", caption
	)

	if data.distribution:
		material.distribution = data.distribution

	set_color(material, 0, data.color)
	set_value(material, 1, data.roughness)
	set_value(material, 2, data.ior)
	set_value(material, 3, data.normal)


def create_glossy_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeBsdfAnisotropic", "Glossy BSDF", caption
	)

	if data.distribution:
		material.distribution = data.distribution

	set_color(material, 0, data.color)
	set_value(material, 1, data.roughness)
	set_value(material, 2, data.anisotropic)
	set_value(material, 3, data.rotation)
	set_value(material, 4, data.normal)
	set_value(material, 5, data.tangent)


def create_principled_bsdf_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeBsdfPrincipled", "Principled BSDF", caption
	)

	if data.subsurface_method:
		material.subsurface_method = data.subsurface_method

	set_color(material, 0, data.color)
	set_value(material, 1, data.metallic)
	set_value(material, 2, data.roughness)
	set_value(material, 3, data.ior)
	set_value(material, 4, data.alpha)
	set_value(material, 5, data.normal)
	#TODO find the input 6
	set_value(material, 7, data.diffuse_roughness)
	set_value(material, 8, data.subsurface_weight)
	set_value(material, 9, data.subsurface_radius)
	set_value(material, 10, data.subsurface_scale)
	set_value(material, 11, data.subsurface_ior)
	set_value(material, 12, data.subsurface_anisotropy)
	set_value(material, 13, data.specular_ior_level)
	set_value(material, 14, data.specular_tint)
	set_value(material, 15, data.anisotropic)
	set_value(material, 16, data.anisotropic_rotation)
	set_value(material, 17, data.tangent)
	set_value(material, 18, data.transmission_weight)
	set_value(material, 19, data.coat_weight)
	set_value(material, 20, data.coat_roughness)
	set_value(material, 21, data.coat_ior)
	set_value(material, 22, data.coat_tint)
	set_value(material, 23, data.coat_normal)
	set_value(material, 24, data.sheen_weight)
	set_value(material, 25, data.sheen_roughness)
	set_value(material, 26, data.sheen_tint)
	set_value(material, 27, data.emission_color)
	set_value(material, 28, data.emission_strength)
	set_value(material, 29, data.thin_film_thickness)
	set_value(material, 30, data.thin_film_ior)


def create_principled_volum_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeVolumePrincipled", "Principled Volume", caption
	)

	set_color(material, 0, data.color)
	set_value(material, 1, data.color_attribute)
	set_value(material, 2, data.density)
	set_value(material, 3, data.density_attribute)
	set_value(material, 4, data.anisotropic)
	set_color(material, 5, data.absorption_color)
	set_value(material, 6, data.emission_strength)
	set_color(material, 7, data.emission_color)
	set_value(material, 8, data.blackbody_intensity)
	set_color(material, 9, data.blackbody_tint)
	set_value(material, 10, data.temperature)
	set_value(material, 11, data.temperature_attribute)


def create_refraction_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeBsdfRefraction", "Refraction BSDF", caption
	)

	if data.distribution:
		material.distribution = data.distribution

	set_color(material, 0, data.color)
	set_value(material, 1, data.roughness)
	set_value(material, 2, data.ior)
	set_value(material, 3, data.normal)


def create_specular_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeEeveeSpecular", "Specular BSDF", caption
	)

	set_color(material, 0, data.color)
	set_value(material, 1, data.specular)
	set_value(material, 2, data.roughness)
	set_color(material, 3, data.emissive_color)
	set_value(material, 4, data.transparency)
	set_value(material, 5, data.normal)
	set_value(material, 6, data.clear_coat)
	set_value(material, 7, data.clear_coat_roughness)
	set_value(material, 8, data.clear_coat_normal)


def create_subsurface_scattering_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeSubsurfaceScattering",
		"Subsurface Scattering", caption
	)

	if data.falloff:
		material.falloff = data.falloff

	set_color(material, 0, data.color)
	set_value(material, 1, data.scale)
	set_value(material, 2, data.radius)
	set_value(material, 3, data.ior)
	set_value(material, 4, data.roughness)
	set_value(material, 5, data.anisotropic)
	set_value(material, 6, data.normal)


def create_translucent_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeBsdfTranslucent", "Translucent BSDF", caption
	)

	set_color(material, 0, data.color)
	set_value(material, 1, data.normal)


def create_transparent_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeBsdfTransparent", "Transparent BSDF", caption
	)

	set_color(material, 0, data.color)


def create_volum_absorption_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeVolumeAbsorption", "Volume Absorption", caption
	)

	set_color(material, 0, data.color)
	set_value(material, 1, data.density)


def create_volum_scatter_material(ctx, caption, data):
	material = create_material_node(
		ctx, data, "ShaderNodeVolumeScatter", "Volume Scatter", caption
	)

	if data.phase:
		material.phase = data.phase

	set_color(material, 0, data.color)
	set_value(material, 1, data.density)
	set_value(material, 2, data.anisotropic)


def create_material(ctx, caption, data):
	if not ctx.object.active_material:
		return

	ctx.object.active_material.use_nodes = True
	if data.type == 'Metallic BSDF':
		create_metallic_material(ctx, caption, data)
	
	elif data.type == "Diffuse BSDF":
		create_diffuse_material(ctx, caption, data)
	
	elif data.type == "Emission":
		create_emssion_material(ctx, caption, data)

	elif data.type == "Glass BSDF":
		create_glass_material(ctx, caption, data)

	elif data.type == "Glossy BSDF":
		create_glossy_material(ctx, caption, data)
	
	elif data.type == "Principled Volume":
		create_principled_volum_material(ctx, caption, data)

	elif data.type == "Refraction BSDF":
		create_refraction_material(ctx, caption, data)

	elif data.type == "Specular BSDF":
		create_specular_material(ctx, caption, data)

	elif data.type == "Subsurface Scattering":
		create_subsurface_scattering_material(ctx, caption, data)

	elif data.type == "Translucent BSDF":
		create_translucent_material(ctx, caption, data)

	elif data.type == "Transparent BSDF":
		create_transparent_material(ctx, caption, data)

	elif data.type == "Volume Absorption":
		create_volum_absorption_material(ctx, caption, data)

	elif data.type == "Volume Scatter":
		create_volum_scatter_material(ctx, caption, data)

	else: #"Principled BSDF" by default
		create_principled_bsdf_material(ctx, caption, data)