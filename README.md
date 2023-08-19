# tga-verify

Script to verify Wii U meta images for use in custom channels

## Notes

This is originally based on [Zarklord's TgaVerify](https://gbatemp.net/threads/450997), this is merely an update and rewrite.

This isn't as needed anymore, as homebrew is generally distributed through WUHBs for use with Aroma.

## Usage

This script checks for the following files: `iconTex.tga`, `bootTvTex.tga`, `bootDrcTex.tga`, `bootLogoTex.tga`

Put the script (`tga-verify.py`) is the same folder as your meta images, and run it.

## Image Requirements

- All images must be uncompressed
- `iconTex.tga` and `bootLogoTex.tga` must be in 32-bit depth
- `bootTvTex.tga` and `bootDrcTex.tga` must be in 24-bit depth
- All images must end with `TRUEVISION-XFILE` (the script will do it for you)

### Image Resolutions

- `iconTex.tga`: 128x128
- `bootLogoTex.tga`: 170x42
- `bootDrcTex.tga`: 854x480
- `bootTvTex.tga`: 1280x720


