# PSSH Structure

| Field Name           | Size(bytes)                   | Description                |
| -------------------- | ----------------------------- | -------------------------- |
| Box size             | 4                             | PSSH box의 전체 사이즈     |
| Box Type             | 4                             | 고정값 0x70 0x73 0x73 0x68 |
| Box version          | 1                             | Box 의 버전                |
| Box flags            | 3                             | Box의 flag 값              |
| DRM System ID        | 16                            | DRM의 System ID            |
| Key ID Count         | 4                             | Key ID의 개수              |
| Key ID Data array    | (Key ID Count) *  16          | Key ID의 배열              |
| DRM System Data Size | 4                             | DRM System Data의 길이     |
| DRM System Data      | Value of DRM System Data size | DRM System Data            |



# Specific System ID 



| Identifier                             | Reference                                                    | Comment                                                      |
| -------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `6dd8b3c3-45f4-4a68-bf3a-64168d01a4a6` | [ABV DRM (MoDRM)](https://www.abvtc.com/)                    | For further information please contact ABV International Pte Ltd. Documentation is available under NDA. ABV Content Protection for MPEG DASH (MoDRM v4.7 and above). |
| `f239e769-efa3-4850-9c16-a903c6932efb` | [Adobe Primetime DRM version 4](https://www.adobe.com/)      | For further information please contact Adobe.                |
| `616c7469-6361-7374-2d50-726f74656374` | [Alticast](https://www.alticast.com/)                        | For further information please contact Alticast. galtiprotect_drm@alticast.com. |
| `94ce86fb-07ff-4f43-adb8-93d2fa968ca2` | [Apple FairPlay](https://developer.apple.com/streaming/fps/) | Content Protection System Identifier for Apple FairPlay Streaming. |
| `279fe473-512c-48fe-ade8-d176fee6b40f` | [Arris Titanium](https://dashif.org/identifiers/content_protection/) | For further information please contact multitrust.info@arris.com. Documentation is available under NDA. @value is specified in documentation related to a specific version of the product. |
| `3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c` | [ChinaDRM](http://www.chinadrmlab.org/)                      | ChinaDRM is defined by China Radio and Television Film Industry Standard GY/T 277-2014. @value indicates ChinaDRM specific solution provided by various vendors. |
| `3ea8778f-7742-4bf9-b18b-e834b2acbd47` | [Clear Key AES-128](https://dashif.org/identifiers/content_protection/) | Identifier for HLS Clear Key encryption using CBC mode. This is to be used as an identifier when requesting key system information when using CPIX. |
| `be58615b-19c4-4684-88b3-c8c57e99e957` | [Clear Key SAMPLE-AES](https://dashif.org/identifiers/content_protection/) | Identifier for HLS Clear Key encryption using CBCS mode. This is to be used as an identifier when requesting key system information when using CPIX. |
| `e2719d58-a985-b3c9-781a-b030af78d30e` | [Clear Key DASH-IF](https://dashif.org/guidelines/)          | This identifier is meant to be used to signal the availability of W3C Clear Key in the context of a DASH presentation. |
| `644fe7b5-260f-4fad-949a-0762ffb054B4` | [CMLA (OMA DRM)](http://www.cm-la.com/)                      | A draft version of the CMLA Technical Specification which is in process with involved adopters is not published. It is planned to be chapter 18 of our CMLA Technical Specification upon completion and approval.Revisions of the CMLA Technical Specification become public upon CMLA approval. UUID will correlate to various related XML schema and PSSH components as well as elements of the content protection element relating to CMLA DASH mapping. |
| `37c33258-7b99-4c7e-b15d-19af74482154` | [Commscope Titanium V3](https://www.commscope.com/product-type/video-processing-security-delivery-systems/content-security-services-software/conditional-access-systems/titanium-cas) | Documentation available under NDA. @value is specified in documentation related to a specific version of the product. Contact multitrust.info@arris.com for further information. |
| `45d481cb-8fe0-49c0-ada9-ab2d2455b2f2` | [CoreCrypt](http://www.coretrust.com/en/products_eurycrypt.asp) | CoreTrust Content Protection for MPEG-DASH. For further information and specification please contact CoreTurst at mktall@coretrust.com. |
| `dcf4e3e3-62f1-5818-7ba6-0a6fe33ff3dd` | [DigiCAP SmartXess](http://www.digicaps.com/?lang=en)        | For further information please contact DigiCAP. Documentation is available under NDA. DigiCAP SmartXess for DASH @value CA/DRM_NAME VERSION (CA 1.0, DRM+ 2.0) |
| `35bf197b-530e-42d7-8b65-1b4bf415070f` | [DivX DRM Series 5](https://dashif.org/identifiers/content_protection/) | Please contact DivX for specifications.                      |
| `80a6be7e-1448-4c37-9e70-d5aebe04c8d2` | [Irdeto Content Protection](https://www.irdeto.com/)         | For further information please contact Irdeto. Documentation is available under NDA. |
| `5e629af5-38da-4063-8977-97ffbd9902d4` | [Marlin Adaptive Streaming Simple Profile V1.0](https://www.marlin-community.com/) | Details of what can be further specified within the ContentProtection element is in the specifications. |
| `9a04f079-9840-4286-ab92-e65be0885f95` | [Microsoft PlayReady](https://www.microsoft.com/playready/documents/) | For further information please contact Microsoft.            |
| `6a99532d-869f-5922-9a91-113ab7b1e2f3` | [MobiTV DRM](https://www.mobitv.com/core-technologies/digital-rights-management/) | Identifier for any version of MobiDRM (MobiTV DRM). The version is signaled in the pssh box. |
| `adb41c24-2dbf-4a6d-958b-4457c0d27b95` | [Nagra MediaAccess PRM 3.0](https://dtv.nagra.com/inquire)   | It identifies Nagra MediaAccess PRM 3.0 and above. Documentation is available under NDA. |
| `1f83e1e8-6ee9-4f0d-ba2f-5ec4e3ed1a66` | [SecureMedia](https://www.securemedia.com/)                  | Documentation is available under NDA. @value shall be Arris SecureMedia version XXXXXXX. XXXXXX is specified in documentation associated with a particular version of the product. The UUID will be made available in SecureMedia documentation shared with a partner or customer of SecureMedia Arris. |
| `992c46e6-c437-4899-b6a0-50fa91ad0e39` | [SecureMedia SteelKnot](https://www.securemedia.com/)        | Documentation is available under NDA. @value shall be Arris SecureMedia SteelKnot version XXXXXXX. The exact length and syntax of XXXXXXX is specified in documentation associated with a particular version of the product. The UUID will be made available in SecureMedia SteelKnot documentation shared with a partner or customer of SecureMedia SteelKnot. |
| `a68129d3-575b-4f1a-9cba-3223846cf7c3` | [Synamedia/Cisco/NDS VideoGuard DRM](https://www.synamedia.com/video-solutions/video-security/) | Documentation is available under NDA.                        |
| `aa11967f-cc01-4a4a-8e99-c5d3dddfea2d` | [Unitend DRM (UDRM)](https://www.unitend.com/)               | For further information please contact y.ren@unitend.com.    |
| `9a27dd82-fde2-4725-8cbc-4234aa06ec09` | [Verimatrix VCAS](https://dashif.org/identifiers/content_protection/) | @value is Verimatrix VCAS for DASH ViewRightWeb VV.vv (VV.vv is the version number). If used this can help the client to determine if the current DRM client can play the content. |
| `b4413586-c58c-ffb0-94a5-d4896c1af6c3` | [Viaccess-Orca DRM (VODRM)](https://www.viaccess-orca.com/drm-solutions) | For further information please contact Viaccess-Orca. VODRM documentation is available under NDA. |
| `793b7956-9f94-4946-a942-23e7ef7e44b4` | [VisionCrypt](https://www.gospell.com/)                      | For further information please contact gosdrm@gospell.com.   |
| `1077efec-c0b2-4d02-ace3-3c1e52e2fb4b` | [W3C Common PSSH box](https://w3c.github.io/encrypted-media/format-registry/initdata/cenc.html) | This identifier is to be used as the SystemID for the Common PSSH box format defined by W3C as a preferred alternative to DRM system specific PSSH box formats. This identifier may be used in PSSH boxes and MPEG-DASH ContentProtection elements. |
| `edef8ba9-79d6-4ace-a3c8-27dcd51d21ed` | [Widevine Content Protection](https://www.widevine.com/)     | For further information please contact Widevine.             |

ref : https://scienceon.kisti.re.kr/commons/util/originalView.do?dbt=TRKO&cn=TRKO201600001185, https://dashif.org/identifiers/content_protection/