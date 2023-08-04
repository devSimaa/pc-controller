from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


def set_volume(volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume.__iid__, comtypes.CLSCTX_ALL, None
    )
    volume_object = cast(interface, POINTER(ISimpleAudioVolume))
    volume_object.SetMasterVolume(volume, None)


# Изменение громкости на 50% (0.5) - можно указать другое значение от 0.0 до 1.0
set_volume(0.5)
