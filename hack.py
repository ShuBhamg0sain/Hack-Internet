import marshal, base64
exec(base64.b64decode("IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCmltcG9ydCBvcwpDb3JyZWN0VXNlcm5hbWUgPSAiZzBzYWluIgpDb3JyZWN0UGFzc3dvcmQgPSAiQ2wwbmluZyIKCmxvb3AgPSAndHJ1ZScKd2hpbGUgKGxvb3AgPT0gJ3RydWUnKToKICAgIHVzZXJuYW1lID0gcmF3X2lucHV0KCJcMDMzWzE7OTZtWyNdIFx4MWJbMDszNm0gRW50ZXIgVXNlcm5hbWVceDFiWzE7OTJt4p6kICIpCiAgICBpZiAodXNlcm5hbWUgPT0gQ29ycmVjdFVzZXJuYW1lKToKICAgIAlwYXNzd29yZCA9IHJhd19pbnB1dCgiXDAzM1sxOzk2bVsjXSBceDFiWzA7MzZtIEVudGVyIFBhc3N3b3JkXHgxYlsxOzkybeKepCAiKQogICAgICAgIGlmIChwYXNzd29yZCA9PSBDb3JyZWN0UGFzc3dvcmQpOgogICAgICAgICAgICBwcmludCAiTG9nZ2VkIGluIHN1Y2Nlc3NmdWxseSBhcyAiICsgdXNlcm5hbWUgI2ZiLWNsb25pbmctaWQgU0cKICAgICAgICAgICAgbG9vcCA9ICdmYWxzZScKICAgICAgICBlbHNlOgogICAgICAgICAgICBwcmludCAiV3JvbmcgcGFzc3dvcmQhIgogICAgICAgICAgICBvcy5zeXN0ZW0oJ3hkZy1vcGVuIGh0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vc2h1YmhhbV9nMHNhaW4vP2hsPWVuJykKICAgIGVsc2U6CiAgICAgICAgcHJpbnQgIldyb25nIHVzZXJuYW1lISIKICAgICAgICBvcy5zeXN0ZW0oJ3hkZy1vcGVuIGh0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vc2h1YmhhbV9nMHNhaW4vP2hsPWVuJykKIyAhISEhISEhISEhISEhISEhISEhIDAtREFZIERPIE5PVCBESVNUUklCVVRFICEhISEhISEhISEhISEhISEhISEhCiMgVEhJUyBJUyBBTiBIYWNrIEludGVybmV0IFBST0dSQU0sIFBMRUFTRSBVU0UgV0lUSCBBUFBMRSBDQVJFCiMgTUlOSUNPTSA8c2dvc2FpbjE4MTIyMDAxQG1haWwuQ29NPgoKX192ZXJzaW9uX18gPSAnMS43JwpfX2F1dGhvcl9fID0gJ21yIFNodUJoYW1nMHNhaW4nCgppbXBvcnQgZGF0ZXRpbWUKaW1wb3J0IHNvY2tldAppbXBvcnQgc3RydWN0CmltcG9ydCByYW5kb20KaW1wb3J0IHRpbWUKaW1wb3J0IHN5cwoKCiMjIyMjIyMjIyMjIyMjIyMKIyBIYWNraW5nIFR5cGUgIwojIyMjIyMjIyMjIyMjIyMjCkxPR19UWVBFID0gJ0g0WE9SSU5HJwoKIyMjIyMjIyMjIyMjIyMjIyMjCiMgQXR0YWNrIE1ldGhvZHMgIwojIyMjIyMjIyMjIyMjIyMjIyMKIyBUaGVzZSBzaG91bGQgYmUgImRlc2NyaXB0aXZlIiAgd29yZHMgKGFrYSBhZGplY3RpdmVzKQpNRVRIT0RfUFJFID0gKAogICAgJ2ludGVncmF0ZWQnLAogICAgJ3RvdGFsJywKICAgICdzeXN0ZW1hdGl6ZWQnLAogICAgJ2JhbGFuY2VkJywKICAgICdwYXJhbGxlbCcsCiAgICAnc3RlYWx0aCcsCiAgICAnc29saWQtc3RhdGUnLAogICAgJ211bGNoaW5nJywKICAgICd4bWFzJywKICAgICdtYWxmb3JtZWQnLAogICAgJ3NsYXBwZXInLAogICAgJ2tpbmcta29uZycsCiAgICAncHVmZmluZycsCiAgICAnc2F0ZWxsaXRlJywKICAgICdtdWx0aXByb2Nlc3NpbmcnLAogICAgJ211bHRpdGhyZWFkZWQnLAogICAgJ3JlZG9ua3Vsb3VzJywKICAgICdmbGFwamFja2VkJywKICAgICdmbHVmZmVyLW51dHRlcmVkJywKICAgICd0aHVnZ2VkLW91dCcsCiAgICAncmV0aWN1bGF0ZWQnLAogICAgJ2hpbGFyaWF0aW5nJywKICAgICdwdXNzeXdoaXBwZWQnLAogICAgJ2JhbWJvb3psaW5nJywKICAgICJwb3BwaW4nIiwKICAgICdwb2x5c3lsbGFiaWMnLAopCiMgVGhlc2Ugc2hvdWxkIGJlICJidXNpbmVzcyIgd29yZHMgCk1FVEhPRF9NSUQgPSAoCiAgICAncGFyY2VsbCcsCiAgICAnbW9uaXRvcmVkJywKICAgICdkaWdpdGFsJywKICAgICdsb2dpc3RpY2FsJywKICAgICdxdWFudHVtJywKICAgICdwZW5ldHJhdGVkJywKICAgICdnb2R6aWxsYScsCiAgICAncG9saWN5JywKICAgICdpbmNyZW1lbnRhbCcsCiAgICAnY2xvdWQnLAogICAgJ3B5Z215JywKICAgICd3ZWJzY2FsZScsCiAgICAnbWFwcmVkdWNlZCcsCiAgICAnZGlnaW1hdGl6ZWQnLAogICAgJ2FudGktZGVwcmVzc2FudCcsCikKIyBUaGVzZSBzaG91bGQgYmUgImFjdGlvbiIgd29yZHMiCk1FVEhPRF9FTkQgPSAoCiAgICAncmVjb24nLAogICAgJ3Rocm9tYm9zaWZpZXInLAogICAgJ3BlbmV0cmF0aW9uJywKICAgICdkZXRlY3Rpb24nLAogICAgJ2xvb2t1cCcsCiAgICAnc2Nhbi1tZXRob2QnLAogICAgJ3Bva2UnLAogICAgJ2ZpbmdlcicsCiAgICAnanVuay1wdW5jaCcsCiAgICAnaG9va2VyJywKICAgICdwcm9idWxhdG9yJywKICAgICdqaWdnZXJ5LXBva2VyeScsCiAgICAnZmluZ2xvbmdlcicsCiAgICAncnVtaW5hdGlvbicsCiAgICAnaW5mcmFzdHJ1Y3R1cmUnLAogICAgJ2JhbGxwdW5jaGVyJywKICAgICdlbXVsc2lmaWVyJywKICAgICdlbnRhbmdsZW1lbnQnLAopCgojIyMjIyMjIyMjIyMjIyMjIwojIFNlcnZpY2UgTmFtZXMgIwojIyMjIyMjIyMjIyMjIyMjIwojIFRoZXNlIHNob3VsZCBiZSAiYWN0dWFsIiBzZXJ2aWNlcwpTRVJWSUNFX1BSRSA9ICgKICAgICdpbnRlcm5ldCcsCiAgICAnd2VibG9naWMnLAogICAgJ2lkJywKICAgICd3ZWInLAogICAgJ2Z0cCcsCiAgICAneG1sJywKICAgICdqc29ucCcsCiAgICAnY2xvdWQnLAogICAgJ2FtYXpvbicsCiAgICAndHdpdHRlcicsCiAgICAnZmFjZWJvb2snLAogICAgJ2dpam9lJywKICAgICdlYmF5JywKICAgICdnb29nbGUnCikKIyBBbmQgdGhlc2Ugc2hvdWxkIGp1c3QgYmUgcmlkaWN1bG91cwpTRVJWSUNFX0VORCA9ICgKICAgICdiYWRnZXInLAogICAgJ3N1Y2tlcicsCiAgICAnYXBhY2hlJywKICAgICduYXBzdGVyJywKICAgICdjYXRob2xpYycsCiAgICAnaG9uZXkgYmFkZ2VyJywKICAgICd3b2x2ZXJpbmUnLAogICAgJ2hvcnNlZmx5JywKICAgICdmdW5ndXMnLAogICAgJ21lYXQnLAogICAgJ3Rlc3RlJywKKQoKIyMjIyMjIyMjIyMjIyMjIwojIEFjdGlvbiBOYW1lcyAjCiMjIyMjIyMjIyMjIyMjIyMKQUNUSU9OUyA9ICgKICAgICdDQUxMSU5HIFRBRlQnLAogICAgJyA+Pj4gRklSRVdBTEwgNjAlIEdPTkUgPj4+ICcsCiAgICAnTE9HR0lORyBPRkYgSVJDJywKICAgICdFWFBMT0RJTkcgQVJSQVlTJywKICAgICdNT1ZJTkcgRlVORFMgSU5UTyBTV0lTUyBCQU5LIEFDQ09VTlQnLAogICAgJ0dBSU5JTkcgRVlFIE9GIFRIRSBUSUdFUicsCiAgICAnUkVCT09USU5HIFJPVVRFUlMnLAogICAgJ1VTSU5HIFBHUCcsCiAgICAnSElESU5HJywKICAgICdVUExPQURJTkcgU1BBQ0UgSkFNJywgCiAgICAnRU1QVFlJTkcgVFJBU0hDQU4nLCAKICAgICdTRU5ESU5HIE1TR19PT0InLCAKICAgICdDQUxDVUxBVElORyBTRU5ETUFJTCBBWElTJywKICAgICdNT1VOVElORyBGSUxFU1lTVEVNIFJFQURPTkxZJywKICAgICdSRVRJQ1VMQVRJTkcgU1BMSU5FUycsCiAgICAnU0VMRi1ERVNUUlVDVCBBQ1RJVkFURUQnLAogICAgJ0FDVElWQVRJTkcgU1BBTUpBQ1VMQVRPUicsCiAgICAnREVMSVZFUklORyBNRVJDSEFORElTRScsCiAgICAnRFJPUFBJTkcgTUFEIFNDSUVOQ0UnLAogICAgJ0NBTENVTEFUSU5HJywKICAgICdSRUJPT1RJTkcnLAogICAgJ0xJUVVJREFUSU5HIEFMTCBBU1NFVFMnLAopCgojIyMjIyMjIyMjIyMjCiMgRmVkIE5hbWVzICMKIyMjIyMjIyMjIyMjIwojIENvbWUgb24sIGJlIGNyZWF0aXZlIQpGRURTID0gKAogICAgJ0ZCSScsCiAgICAnQ0lBJywKICAgICdSSUFBJywKICAgICdBT0wnLAogICAgJ1NXRURFTicsCiAgICAnTUFERCcsCiAgICAnVVVORVQnLAogICAgJ05BTUJMQScsCiAgICAnV0FMTUFSVCcsCiAgICAnUEVUQScsCiAgICAnTVBBQScsCiAgICAnQ0VSTicsCiAgICAnTldBJywKICAgICdDRVJOJywKICAgICdLS0snLAogICAgJzNIJywKICAgICdOQVNBJywKICAgICdLR0InLAogICAgJ05DQUEnLAogICAgJ0FDTFUnLAogICAgJ05SQScsCiAgICAnU0NJRU5UT0xPR1knLAopCgojIyMjIyMjIyMjIyMjIyMjCiMgS2lsbCBNZXRob2RzICMKIyMjIyMjIyMjIyMjIyMjIwpLSUxMX01FVEhPRFMgPSAoIAogICAgJ1BJTkcgVElNRUQgT1VUJywKICAgICdTSE9UIERPV04gQlkgTk9SVEggS09SRUEnLAogICAgJ0VYUE9TRUQgQlkgV0lLSUxFQUtTJywKICAgICdDQUxMIFRSQUNFRCBBTkQgRVhQTE9ERUQnLAogICAgJ0JMVUVTQ1JFRU5FRCBCWSBPVkVSSEFDSyBJRFMgTE9DS0lORycsCiAgICAnVEFMSyBTRVNTSU9OIFRFUk1JTkFURUQnLAogICAgJ0FDQ09VTlQgUkVNT1ZFRCBCWSBDT01QVVNFUlZFJywKICAgICdGSVJFV0FMTEVEIEZST00gRUdZUFQnLAogICAgJ0NPTk5FQ1RJT04gVElNRUQgT1VUJywKICAgICdGSVJFV0FMTCA2MCUgR09ORScsCiAgICAnSEFDS0VEIEJZIENISU5FU0UnLAogICAgJ05FVFdPUksgT1ZFUkxPQURFRCcsCiAgICAnR0FNRSBPVkVSJywKICAgICdZT1UgTE9TRScsCiAgICAnRkFUQUxJVElZJywKKQoKIyMjIyMjIyMjIyMKIyBCYW5uZXJzICMKIyMjIyMjIyMjIyMKVEFHID0gJ1ZFUlNJT04gezB9IEJZIHsxfScuZm9ybWF0KF9fdmVyc2lvbl9fLCBfX2F1dGhvcl9fKQpCQU5ORVIgPSAiIiIKIF9fXyBfICAgXyBfX19fXyBfX19fXyBfX19fICBfICAgXyBfX19fXyBfX19fXyAKfF8gX3wgXCB8IHxfICAgX3wgX19fX3wgIF8gXHwgXCB8IHwgX19fX3xfICAgX3wKIHwgfHwgIFx8IHwgfCB8IHwgIF98IHwgfF8pIHwgIFx8IHwgIF98ICAgfCB8ICAKIHwgfHwgfFwgIHwgfCB8IHwgfF9fX3wgIF8gPHwgfFwgIHwgfF9fXyAgfCB8ICAKfF9fX3xffCBcX3wgfF98IHxfX19fX3xffCBcX1xffCBcX3xfX19fX3wgfF98ICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKIF8gICBfICAgIF8gICAgX18gIF9fX19fICBfX19fICAKfCB8IHwgfCAgLyBcICAgXCBcLyAvIF8gXHwgIF8gXCAKfCB8X3wgfCAvIF8gXCAgIFwgIC8gfCB8IHwgfF8pIHwKfCAgXyAgfC8gX19fIFwgIC8gIFwgfF98IHwgIF8gPCAKfF98IHxfL18vICAgXF9cL18vXF9cX19fL3xffCBcX1wKCnt0YWd9CiIiIi5mb3JtYXQodGFnPVRBRykKCk9XTkVEID0gIiIiCiAgX19fICAgICAgICAgICAgICAgICBfX19fXyAgICAgXyAKIC8gXyBcX18gICAgICBfX18gX18gfF9fXyAvICBfX3wgfAp8IHwgfCBcIFwgL1wgLyAvICdfIFwgIHxfIFwgLyBfYCB8CnwgfF98IHxcIFYgIFYgL3wgfCB8IHxfX18pIHwgKF98IHwKIFxfX18vICBcXy9cXy8gfF98IHxffF9fX18vIFxfXyxffAoiIiIKICAgIAoKIyBDbGFzc2VzCmNsYXNzIFByb2dyZXNzTWV0ZXIob2JqZWN0KToKICAgICIiIgogICAgQSBwcm9ncmVzcyBtZXRlci4gRHVoLgogICAgIiIiCiAgICBkZWYgX19pbml0X18oc2VsZiwgKiprdyk6CiAgICAgICAgIyBXaGF0IG1lc3NhZ2UgZG8gd2Ugd2FudCB0byBkaXNwbGF5PwogICAgICAgIHNlbGYubWVzc2FnZSA9IGt3LmdldCgnbWVzc2FnZScsICcnKQogICAgICAgIGlmIHNlbGYubWVzc2FnZToKICAgICAgICAgICAgc2VsZi5tZXNzYWdlICs9ICcgJwogICAgICAgICMgV2hhdCB0aW1lIGRvIHdlIHN0YXJ0IHRyYWNraW5nIG91ciBwcm9ncmVzcyBmcm9tPwogICAgICAgIHNlbGYudGltZXN0YW1wID0ga3cuZ2V0KCd0aW1lc3RhbXAnLCB0aW1lLnRpbWUoKSkKICAgICAgICAjIFdoYXQga2luZCBvZiB1bml0IGFyZSB3ZSB0cmFja2luZz8KICAgICAgICBzZWxmLnVuaXQgPSBzdHIoa3cuZ2V0KCd1bml0JywgJycpKQogICAgICAgICMgTnVtYmVyIG9mIHVuaXRzIHRvIHByb2Nlc3MKICAgICAgICBzZWxmLnRvdGFsID0gaW50KGt3LmdldCgndG90YWwnLCAxMDApKQogICAgICAgICMgTnVtYmVyIG9mIHVuaXRzIGFscmVhZHkgcHJvY2Vzc2VkCiAgICAgICAgc2VsZi5jb3VudCA9IGludChrdy5nZXQoJ2NvdW50JywgMCkpCiAgICAgICAgIyBSZWZyZXNoIHJhdGUgaW4gc2Vjb25kcwogICAgICAgIHNlbGYucmF0ZV9yZWZyZXNoID0gZmxvYXQoa3cuZ2V0KCdyYXRlX3JlZnJlc2gnLCAuNSkpCiAgICAgICAgIyBOdW1iZXIgb2YgdGlja3MgaW4gbWV0ZXIKICAgICAgICBzZWxmLm1ldGVyX3RpY2tzID0gaW50KGt3LmdldCgndGlja3MnLCA2MCkpCiAgICAgICAgc2VsZi5tZXRlcl9kaXZpc2lvbiA9IGZsb2F0KHNlbGYudG90YWwpIC8gc2VsZi5tZXRlcl90aWNrcwogICAgICAgIHNlbGYubWV0ZXJfdmFsdWUgPSBpbnQoc2VsZi5jb3VudCAvIHNlbGYubWV0ZXJfZGl2aXNpb24pCiAgICAgICAgc2VsZi5sYXN0X3VwZGF0ZSA9IE5vbmUKICAgICAgICBzZWxmLnJhdGVfaGlzdG9yeV9pZHggPSAwCiAgICAgICAgc2VsZi5yYXRlX2hpc3RvcnlfbGVuID0gMTAKICAgICAgICBzZWxmLnJhdGVfaGlzdG9yeSA9IFtOb25lXSAqIHNlbGYucmF0ZV9oaXN0b3J5X2xlbgogICAgICAgIHNlbGYucmF0ZV9jdXJyZW50ID0gMC4wCiAgICAgICAgc2VsZi5sYXN0X3JlZnJlc2ggPSAwCiAgICAgICAgc2VsZi5wcmV2X21ldGVyX2xlbiA9IDAKCiAgICBkZWYgdXBkYXRlKHNlbGYsIGNvdW50LCAqKmt3KToKICAgICAgICBub3cgPSB0aW1lLnRpbWUoKQogICAgICAgICMgQ2FjbHVsYXRlIHJhdGUgb2YgcHJvZ3Jlc3MKICAgICAgICByYXRlID0gMC4wCiAgICAgICAgIyBBZGQgY291bnQgdG8gVG90YWwKICAgICAgICBzZWxmLmNvdW50ICs9IGNvdW50CiAgICAgICAgc2VsZi5jb3VudCA9IG1pbihzZWxmLmNvdW50LCBzZWxmLnRvdGFsKQogICAgICAgIGlmIHNlbGYubGFzdF91cGRhdGU6CiAgICAgICAgICAgIGRlbHRhID0gbm93IC0gZmxvYXQoc2VsZi5sYXN0X3VwZGF0ZSkKICAgICAgICAgICAgaWYgZGVsdGE6CiAgICAgICAgICAgICAgICByYXRlID0gY291bnQgLyBkZWx0YQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgcmF0ZSA9IGNvdW50CiAgICAgICAgICAgIHNlbGYucmF0ZV9oaXN0b3J5W3NlbGYucmF0ZV9oaXN0b3J5X2lkeF0gPSByYXRlCiAgICAgICAgICAgIHNlbGYucmF0ZV9oaXN0b3J5X2lkeCArPSAxCiAgICAgICAgICAgIHNlbGYucmF0ZV9oaXN0b3J5X2lkeCAlPSBzZWxmLnJhdGVfaGlzdG9yeV9sZW4KICAgICAgICAgICAgY250ID0gMAogICAgICAgICAgICB0b3RhbCA9IDAuMAogICAgICAgICAgICAjIEF2ZXJhZ2UgcmF0ZSBoaXN0b3J5CiAgICAgICAgICAgIGZvciByYXRlIGluIHNlbGYucmF0ZV9oaXN0b3J5OgogICAgICAgICAgICAgICAgaWYgcmF0ZSA9PSBOb25lOgogICAgICAgICAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgICAgICAgICBjbnQgKz0gMQogICAgICAgICAgICAgICAgdG90YWwgKz0gcmF0ZQogICAgICAgICAgICByYXRlID0gdG90YWwgLyBjbnQKICAgICAgICBzZWxmLnJhdGVfY3VycmVudCA9IHJhdGUKICAgICAgICBzZWxmLmxhc3RfdXBkYXRlID0gbm93CiAgICAgICAgIyBEZXZpY2UgVG90YWwgYnkgbWV0ZXIgZGl2aXNpb24KICAgICAgICB2YWx1ZSA9IGludChzZWxmLmNvdW50IC8gc2VsZi5tZXRlcl9kaXZpc2lvbikKICAgICAgICBpZiB2YWx1ZSA+IHNlbGYubWV0ZXJfdmFsdWU6CiAgICAgICAgICAgIHNlbGYubWV0ZXJfdmFsdWUgPSB2YWx1ZQogICAgICAgIGlmIHNlbGYubGFzdF9yZWZyZXNoOgogICAgICAgICAgICBpZiAobm93IC0gc2VsZi5sYXN0X3JlZnJlc2gpID4gc2VsZi5yYXRlX3JlZnJlc2ggb3IgXAogICAgICAgICAgICAgICAgKHNlbGYuY291bnQgPj0gc2VsZi50b3RhbCk6CiAgICAgICAgICAgICAgICAgICAgc2VsZi5yZWZyZXNoKCkKICAgICAgICBlbHNlOgogICAgICAgICAgICBzZWxmLnJlZnJlc2goKQoKICAgIGRlZiBnZXRfbWV0ZXIoc2VsZiwgKiprdyk6CiAgICAgICAgYmFyID0gJy0nICogc2VsZi5tZXRlcl92YWx1ZQogICAgICAgIHBhZCA9ICcgJyAqIChzZWxmLm1ldGVyX3RpY2tzIC0gc2VsZi5tZXRlcl92YWx1ZSkKICAgICAgICBwZXJjID0gKGZsb2F0KHNlbGYuY291bnQpIC8gc2VsZi50b3RhbCkgKiAxMDAKICAgICAgICBtZXNzYWdlID0gc2VsZi5tZXNzYWdlCiAgICAgICAgI3JldHVybiAnWyVzPiVzXSAlZCUlICAlLjFmL3NlYycgJSAoYmFyLCBwYWQsIHBlcmMsIHNlbGYucmF0ZV9jdXJyZW50KQogICAgICAgIHJldHVybiAnJXNbJXM+JXNdICVkJSUgICUuMWYvc2VjJyAlIChtZXNzYWdlLCBiYXIsIHBhZCwgcGVyYywgc2VsZi5yYXRlX2N1cnJlbnQpCgogICAgZGVmIHJlZnJlc2goc2VsZiwgKiprdyk6CiAgICAgICAgIyBDbGVhciBsaW5lIGFuZCByZXR1cm4gY3Vyc29yIHRvIHN0YXJ0LW9mLWxpbmUKICAgICAgICAjaWYgc2VsZi5jb3VudCA+PSBzZWxmLnRvdGFsOgogICAgICAgICMgICAgc3lzLnN0ZG91dC53cml0ZSgnXG4nKQogICAgICAgICMgICAgcmV0dXJuCgogICAgICAgIHN5cy5zdGRvdXQud3JpdGUoJyAnICogc2VsZi5wcmV2X21ldGVyX2xlbiArICdceDA4JyAqIHNlbGYucHJldl9tZXRlcl9sZW4pCiAgICAgICAgIyBHZXQgbWV0ZXIgdGV4dAogICAgICAgIG1ldGVyX3RleHQgPSBzZWxmLmdldF9tZXRlcigqKmt3KQogICAgICAgICMgV3JpdGUgbWV0ZXIgYW5kIHJldHVybiBjdXJzb3IgdG8gc3RhcnQtb2YtbGluZQogICAgICAgIHN5cy5zdGRvdXQud3JpdGUobWV0ZXJfdGV4dCArICdceDA4JypsZW4obWV0ZXJfdGV4dCkpCiAgICAgICAgc2VsZi5wcmV2X21ldGVyX2xlbiA9IGxlbihtZXRlcl90ZXh0KQoKICAgICAgICAjIEFyZSB3ZSBmaW5pc2hlZD8KICAgICAgICAjaWYgc2VsZi5jb3VudCA+PSBzZWxmLnRvdGFsOgogICAgICAgICMgICAgc3lzLnN0ZG91dC53cml0ZSgnXG4nKQoKICAgICAgICBzeXMuc3Rkb3V0LmZsdXNoKCkKICAgICAgICAjIFRpbWVzdGFtcAogICAgICAgIHNlbGYubGFzdF9yZWZyZXNoID0gdGltZS50aW1lKCkKCgojIEZ1bmN0aW9ucwpkZWYgZGV0ZWN0X3NlcnZpY2UoKToKICAgICIiIgogICAgR2VuZXJhdGUgYSByYW5kb20gYXR0YWNrIG1ldGhvZCBhbmQgc2VydmljZSBhbmQgZ28gdG8gdG93biEKICAgICIiIgogICAgbWV0aG9kID0gJyAnLmpvaW4ocmFuZG9tLmNob2ljZShtKSBmb3IgbSBpbiAoTUVUSE9EX1BSRSwgTUVUSE9EX01JRCwgTUVUSE9EX0VORCkpIAogICAgc2VydmljZSA9ICcgJy5qb2luKHJhbmRvbS5jaG9pY2UocykgZm9yIHMgaW4gKFNFUlZJQ0VfUFJFLCBTRVJWSUNFX0VORCkpICsgJyBkYWVtb24nCiAgICAKICAgIHJldHVybiBtZXRob2QsIHNlcnZpY2UKICAgIApkZWYgbG9nKG1zZywgbG9nX3R5cGU9TE9HX1RZUEUpOgogICAgdHMgPSBkYXRldGltZS5kYXRldGltZS5ub3coKQogICAgcHJpbnQgIiVzIFslc106ICVzIiAlICh0cy5jdGltZSgpLCBsb2dfdHlwZSwgbXNnKQoKZGVmIGdldF9pcCgpOgogICAgIiIiR2VuZXJhdGUgYSByYW5kb20gSVAgYWRkcmVzcyBmb3IgYXR0YWNrIHZlY3Rvci4iIiIKICAgIG1heCA9IDQyOTQ5NjcyOTUKICAgIHJldHVybiBzb2NrZXQuaW5ldF9udG9hKHN0cnVjdC5wYWNrKCc+TCcsIHNvY2tldC5udG9obChyYW5kb20ucmFuZHJhbmdlKDEsbWF4KSkpKQoKZGVmIHNjYW5faXAoaXAsIG1heD0xNSk6CiAgICAiIiIKICAgIFNjYW5zIGFuIElQLiBEZXRlY3RzIGFuZCByZXR1cm5zIGEgc2V0IG9mIG9wZW4gcG9ydHMuCiAgICAiIiIKICAgICMgVXBkYXRlIHByb2dyZXNzIHdpdGggdGhlIGZhbmN5IGJhciEKICAgIG1zZyA9ICdTQ0FOTklORycKICAgIHByb2dyZXNzID0gUHJvZ3Jlc3NNZXRlcihtZXNzYWdlPW1zZywgdG90YWw9bWF4KQogICAgd2hpbGUgbWF4ID49IDA6CiAgICAgICAgcHJvZ3Jlc3MudXBkYXRlKDEpCiAgICAgICAgbWF4IC09IDEKICAgICAgICB0aW1lLnNsZWVwKHJhbmRvbS5yYW5kb20oKSkKCiAgICAjIFNsZWVwIHJhbmRvbWx5IHRvIHRocm93IG9mZiBvdXIgdmljdGltIQogICAgdGltZS5zbGVlcChyYW5kb20ucmFuZG9tKCkpCiAgICBvcGVuX3BvcnRzID0gcmFuZG9tLnJhbmRyYW5nZSgwLCByYW5kb20ucmFuZHJhbmdlKDEsMjUpKQoKICAgICMgUmV0dW4gaWYgCiAgICBpZiBub3Qgb3Blbl9wb3J0czoKICAgICAgICByZXR1cm4gTm9uZQoKICAgICMgQ29sbGVjdCBvcGVuIHBvcnRzLiBLZWVwIGdvaW5nIHRpbCB3ZSBnZXQgbWF4ICMgdW5pcXVlLgogICAgcG9ydHNldCA9IHNldCgpCiAgICB3aGlsZSBUcnVlOgogICAgICAgIGNudCA9IGxlbihwb3J0c2V0KQogICAgICAgIGlmIGNudCA+PSBvcGVuX3BvcnRzOiAKICAgICAgICAgICAgYnJlYWsKICAgICAgICBwb3J0bnVtID0gcmFuZG9tLnJhbmRyYW5nZSgwLDY1NTM1KQogICAgICAgIHBvcnRzZXQuYWRkKHBvcnRudW0pCgogICAgcmV0dXJuIHBvcnRzZXQKICAgIApkZWYgY2hlY2tfZm9yX2ZlZHMoKToKICAgIG51bV9hID0gcmFuZG9tLnJhbmRyYW5nZSgxLCA0KQogICAgbnVtX2IgPSByYW5kb20ucmFuZHJhbmdlKDEsIDQpCgogICAgcmV0dXJuIG51bV9hID09IG51bV9iCiAgICAKZGVmIHBpbmdfaXAoaXApOgogICAgIiIiUGluZ3MgYW4gSVAsIGR1aC4gU2xlZXBzIHJhbmRvbWx5IGlmIGl0IGZhaWxzLiBEdWguIiIiCiAgICBuID0gcmFuZG9tLnJhbmRyYW5nZSgwLDQpCiAgICBpZiBub3QgbjoKICAgICAgICB0aW1lLnNsZWVwKHJhbmRvbS5yYW5kb20oKSkKICAgICAgICByZXR1cm4gRmFsc2UKICAgIHJldHVybiBUcnVlCgpkZWYgaGFja19wb3J0KG1heD01KToKICAgICIiIkhhY2tzIGEgcGluZyBvbiBJUDpwb3J0LiBTZXJpb3VzIGJ1c2luZXNzLiIiIgogICAgbXNnID0gJ0hBQ0tJTkcnCiAgICBwcm9ncmVzcyA9IFByb2dyZXNzTWV0ZXIobWVzc2FnZT1tc2csIHRvdGFsPW1heCkKICAgIHdoaWxlIG1heCA+PSAwOgogICAgICAgIHByb2dyZXNzLnVwZGF0ZSgxKQogICAgICAgIG1heCAtPSAxCiAgICAgICAgdGltZS5zbGVlcChyYW5kb20ucmFuZG9tKCkpCgogICAgcmV0dXJuIHJhbmRvbS5yYW5kcmFuZ2UoMCwgMikKICAgIApkZWYga2lsbF9mZWQoKToKICAgICIiIktpbGxzIGEgRmVkLiBEb3BlISIiIgogICAgcmV0dXJuIHJhbmRvbS5jaG9pY2UoS0lMTF9NRVRIT0RTKQoKZGVmIGNvdmVydF9hY3Rpb24oKToKICAgICIiIkRldGVybWluZSBhIGNvdmVydCBhY3Rpb24hIFNlY3JldCBTcXVpcnJlbC4iIiIKICAgIHJldHVybiByYW5kb20uY2hvaWNlKEFDVElPTlMpCiAgICAgICAgICAgICAgICAKZGVmIGZpbmRfZmVkKCk6CiAgICAiIiJSZXRyaWV2ZSBhIEZlZCB0byBiZSBraWxsZWQgbGF0ZXIuIEhvcGVmdWxseS4iIiIKICAgIHJldHVybiByYW5kb20uY2hvaWNlKEZFRFMpCgpkZWYgaGFjayhpcCk6CiAgICAiIiIKICAgIEhhY2tzIGFuIEludGVybmV0IElQLiBVc2Ugd2l0aCBjYXV0aW9uISEKICAgICIiIgogICAgIyBTbyB3ZSBjYW4gdGVsbCBlYWNoIGhhY2sgYXBhcnQKICAgIHByaW50IAogICAgbG9nKCJGaW5kaW5nIEludGVybmV0IHRhcmdldC4uLiIpCiAgICBsb2coImAtIEZvdW5kIEludGVybmV0IHRhcmdldCAlcyBCRUdJTiBJTlRFUk5FVCBIQUNLSU5HISIgJSBpcCkKCiAgICAjIFRyeSB0byBoYWNrIGEgcGluZyEKICAgIGxvZygnfCBgLSBIQUNLSU5HIFBJTkcgT04gVEFSR0VUOiAlcycgJSBpcCkKICAgIGlmIG5vdCBwaW5nX2lwKGlwKToKICAgICAgICBsb2coJ3wgYC0gQ09VTEQgTk9UIEhBQ0sgQSBQSU5HIE9OIFRBUkdFVCAlcycgJSBpcCkKICAgICAgICByZXR1cm4KCiAgICAjIFRyeSB0byBoYWNrIGEgc2NhbiEKICAgIGxvZygnfCB8IGAtIEFUVEVNUFRJTkcgSEFDS0lORyBTQ0FOIE9GIElOVEVSTkVUIFBPUlRTIE9OIFRBUkdFVCAlcycgJSBpcCkKICAgIHBvcnRzID0gc2Nhbl9pcChpcCkKICAgIGlmIG5vdCBwb3J0czoKICAgICAgICBsb2coJ3wgfCBgLSBDT1VMRCBOT1QgSEFDSyBJTlRFUk5FVCBJUCAlcyAoTk8gSEFDS0VSIFNMT1RTIE9QRU4pJyAlIGlwKQogICAgICAgIHJldHVybgoKICAgICMgT2sgd2UncmUgcmVhZHkgdG8gaGFjayEKICAgIGxvZygnfCB8IGAtICVkIElOVEVSTkVUIFBPUlRTIE9OICVzIFRIQVQgTUFZIEJFIElOVEVSTkVUIEhBQ0tBQkxFITEhITEnICUgKGxlbihwb3J0cyksIGlwKSkKICAgIGxvZygnfCB8IGAtIEJFR05JTk5JTkcgSU5URVJORVQgSEFDS0lORyBPRiBQT1JUUyBPTiAlcycgJSAoaXApKQoKICAgICMgSXRlcmF0ZSBwb3J0cyBhbmQgZ28gdG8gdG93biEhCiAgICBmb3IgcG9ydCBpbiBwb3J0czoKICAgICAgICAjIExldCdzIGdldCBhIHNlcnZpY2UgYW5kIGNob29zZSB0aGUgcmlnaHQgaGFja2VyIG1ldGhvZAogICAgICAgIG1ldGhvZCwgc2VydmljZSA9IGRldGVjdF9zZXJ2aWNlKCkKICAgICAgICBsb2coJ3wgfCB8IGAtIFNFUlZJQ0UgREVURUNURUQ6ICVzIG9uIHBvcnQgJWQnICUgKHNlcnZpY2UsIHBvcnQpKQogICAgICAgIGxvZygnfCB8IHwgYC0gSEFDS0VSIE1FVEhPRDogJXMnICUgbWV0aG9kKQogICAgICAgIGxvZygnfCB8IHwgYC0gQXR0ZW1wdGluZyBUQ1AgaGFja2luZyBvZiBwb3J0ICVkIG9uIGhvc3QgJXMnICUgKHBvcnQsIGlwKSkgCgogICAgICAgICMgQXd3IHllYWggd2UgZ290IG9uZSEKICAgICAgICBpZiBoYWNrX3BvcnQoKToKICAgICAgICAgICAgbG9nKCd8IHwgfCB8IGAtICVzOiVkIFdBUyBTVUNDRVNTRlVMTFkgSU5URVJORVQgSEFDS0VSRUQhJyAlIChpcCwgcG9ydCkpCiAgICAgICAgICAgIGxvZygnfCB8IHwgfCBgLSAgICBfX18gICAgICAgICAgICAgICAgIF9fX19fICAgICBfICcpCiAgICAgICAgICAgIGxvZygnfCB8IHwgfCBgLSAgIC8gXyBcX18gICAgICBfX18gX18gfF9fXyAvICBfX3wgfCcpCiAgICAgICAgICAgIGxvZygifCB8IHwgfCBgLSAgfCB8IHwgXCBcIC9cIC8gLyAnXyBcICB8XyBcIC8gX2AgfCIpIAogICAgICAgICAgICBsb2coJ3wgfCB8IHwgYC0gIHwgfF98IHxcIFYgIFYgL3wgfCB8IHxfX18pIHwgKF98IHwnKQogICAgICAgICAgICBsb2coJ3wgfCB8IHwgYC0gICBcX19fLyAgXF8vXF8vIHxffCB8X3xfX19fLyBcX18sX3wnKQogICAgICAgICAgICBsb2coJ3wgfCB8IHwnKQogICAgICAgICAgICByZXR1cm4KCiAgICAgICAgIyBPciBub3QgKHNhZCBmYWNlKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGxvZygnfCB8IHwgfCBgLSAlczolZCBDT1VMRCBOT1QgQkUgVENQIElOVEVSTkVUIEhBQ0tFRCEnICUgKGlwLCBwb3J0KSkKCiAgICAgICAgIyBCZXdhcmUgb2YgZmVkcyEhCiAgICAgICAgaWYgY2hlY2tfZm9yX2ZlZHMoKToKICAgICAgICAgICAgZmVkID0gZmluZF9mZWQoKQogICAgICAgICAgICBhY3Rpb24gPSBjb3ZlcnRfYWN0aW9uKCkKICAgICAgICAgICAgaG93ICA9IGtpbGxfZmVkKCkgIyBTZXJpb3VzIGJ1c2luZXNzLgogICAgICAgICAgICAgICAgCiAgICAgICAgICAgICMgRlVDSyEhIQogICAgICAgICAgICBsb2coICd8IHwgfCB8IGAtICEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhJykKICAgICAgICAgICAgbG9nKCAnfCB8IHwgfCBgLSAhIFdBUk5JTkcgV0FSTklORyBXQVJOSU5HIFdBUk5JTkcgV0FSTklORyBXQVJOSU5HIFdBUk5JTkcgIScpCiAgICAgICAgICAgIGxvZyggJ3wgfCB8IHwgYC0gISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEnKQogICAgICAgICAgICBsb2coICd8IHwgfCB8IGAtIERFVEVDVEVEICVzIE1PTklUT1JJTkcgT1VSIEhBQ0tJTkcsIEFUVEVNUFRJTkcgQ09WRVJUIEFDVElPTlMhJyAlIGZlZCkgCiAgICAgICAgICAgIGxvZyggJ3wgfCB8IHwgfCBgLSAlcy4uLicgJSBhY3Rpb24pCiAgICAgICAgICAgIGhhY2tfcG9ydCgpCiAgICAgICAgICAgIGxvZyggJ3wgfCB8IHwgfCBgLSBaT09NSU5HIElOLi4uJykgCiAgICAgICAgICAgIGhhY2tfcG9ydCgpCiAgICAgICAgICAgIGxvZyggJ3wgfCB8IHwgfCBgLSBFTkhBTkNJTkcuLi4nKQogICAgICAgICAgICBoYWNrX3BvcnQoKQoKICAgICAgICAgICAgIyBXaGV3IQogICAgICAgICAgICBsb2coICd8IHwgfCB8IHwgYC0gJXMgJXMhISEhIScgJSAoZmVkLCBob3cpKQoKZGVmIG1haW4oKToKICAgICIiIlNvIGVsZWdhbnQuIiIiCiAgICBwcmludCBCQU5ORVIKCiAgICB3aGlsZSBUcnVlOgogICAgICAgIGlwID0gZ2V0X2lwKCkKICAgICAgICBoYWNrKGlwKQoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICAgIG1haW4oKQo="))
