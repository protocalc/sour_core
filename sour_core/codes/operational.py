PTP_OPCODE = {
    'DataType' : 'H',
    'Values': {
        'Undefined'                 : 0x1000,
        'GetDeviceInfo'             : 0x1001,
        'OpenSession'               : 0x1002,
        'CloseSession'              : 0x1003,
        'GetStorageIDs'             : 0x1004,
        'GetStorageInfo'            : 0x1005,
        'GetNumObjects'             : 0x1006,
        'GetObjectHandles'          : 0x1007,
        'GetObjectInfo'             : 0x1008,
        'GetObject'                 : 0x1009,
        'GetThumb'                  : 0x100A,
        'DeleteObject'              : 0x100B,
        'SendObjectInfo'            : 0x100C,
        'SendObject'                : 0x100D,
        'InitiateCapture'           : 0x100E,
        'FormatStore'               : 0x100F,
        'ResetDevice'               : 0x1010,
        'SelfTest'                  : 0x1011,
        'SetObjectProtection'       : 0x1012,
        'PowerDown'                 : 0x1013,
        'GetDevicePropDesc'         : 0x1014,
        'GetDevicePropValue'        : 0x1015,
        'SetDevicePropValue'        : 0x1016,
        'ResetDevicePropValue'      : 0x1017,
        'TerminateOpenCapture'      : 0x1018,
        'MoveObject'                : 0x1019,
        'CopyObject'                : 0x101A,
        'GetPartialObject'          : 0x101B,
        'InitiateOpenCapture'       : 0x101C,
        'StartEnumHandles'          : 0x101D,
        'EnumHandles'               : 0x101E,
        'StopEnumHandles'           : 0x101F,
        'GetVendorExtensionMapss'   : 0x1020,
        'GetVendorDeviceInfo'       : 0x1021,
        'GetResizedImageObject'     : 0x1022,
        'GetFilesystemManifest'     : 0x1023,
        'GetStreamInfo'             : 0x1024,
        'GetStream'                 : 0x1025
        }
    }

MTP_OPCODE = {
    'DataType' : 'H',
    'Values': {
        'GetObjInfo'                : 0x9803,
        'GetObjPropList'            : 0x9805
        }
    }

SONY_OPCODE = {
    'DataType' : 'H',
    'Values' : {
        'SDIOConnect'               : 0x9201,
        'SDIOGetExtDeviceInfo'      : 0x9202,
        'SonyGetDevicePropDesc'     : 0x9203,
        'SonyGetDevicePropValue'    : 0x9204,
        'SetControlDeviceA'         : 0x9205,
        'GetControlDeviceDesc'      : 0x9206,
        'SetControlDeviceB'         : 0x9207,
        'GetAllDevicePropData'      : 0x9209,
        'MTPSession'                : 0x9210,
        'GetFile'                   : 0x9211,
        'SendRequest'               : 0x9212,
        'EnableTrustedFileOp'       : 0x9214
    }
}

OPCODES = [PTP_OPCODE, MTP_OPCODE, SONY_OPCODE]
