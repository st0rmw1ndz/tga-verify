# TGA Verify

Script to verify Wii U meta images for use in custom channels

> [!NOTE]
> This is originally based on [Zarklord's TgaVerify](https://gbatemp.net/threads/450997), this is merely an update and rewrite.
> This isn't as needed anymore, as homebrew is generally distributed through WUHBs for use with Aroma.



## Usage

Put the script in the same folder as your meta images, and run it.

This script checks for the following files: `iconTex.tga`, `bootTvTex.tga`, `bootDrcTex.tga`, `bootLogoTex.tga`

### Image Requirements

- All images must be uncompressed
- All images must end with `TRUEVISION-XFILE` (the script will do it for you)
- `iconTex.tga`: 128x128, 32-bit depth
- `bootLogoTex.tga`: 170x42, 32-bit depth
- `bootDrcTex.tga`: 854x480, 24-bit depth
- `bootTvTex.tga`: 1280x720, 24-bit depth
