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

def rgba_to_hex(color):
	r = int(color[0] * 255)
	g = int(color[1] * 255)
	b = int(color[2] * 255)
	a = int(color[3] * 255)
	return "#{:02X}{:02X}{:02X}{:02X}".format(r, g, b, a)


def srgb_to_linear(c):
	if c <= 0.04045:
		return c / 12.92
	else:
		return ((c + 0.055) / 1.055) ** 2.4


def gamma_correction(color):
	r = srgb_to_linear(color[0])
	g = srgb_to_linear(color[1])
	b = srgb_to_linear(color[2])
	return (r, g, b, color[3])
