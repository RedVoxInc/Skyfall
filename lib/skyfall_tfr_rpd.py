# Python libraries
import matplotlib.pyplot as plt

# RedVox RedPandas and related RedVox modules
import redpandas.redpd_plot.mesh as rpd_plot
import redpandas.redpd_tfr as rpd_tfr
from libquantum.plot_templates import plot_time_frequency_reps as pnl
import lib.skyfall_dw as sf_dw

# Configuration file
from skyfall_config_file import skyfall_config, tfr_config

axes = ["X", "Y", "Z"]


def main():
    """
    RedVox RedPandas time-frequency representation of API900 data. Example: Skyfall.
    Last updated: 20210909
    """
    print('Let the sky fall...')

    # Label columns in dataframe
    station_label: str = "station_id"

    # Audio columns
    audio_data_label: str = "audio_wf"
    audio_epoch_s_label: str = "audio_epoch_s"
    audio_fs_label: str = "audio_sample_rate_nominal_hz"
    audio_tfr_bits_label: str = "audio_tfr_bits"
    audio_tfr_frequency_hz_label: str = "audio_tfr_frequency_hz"
    audio_tfr_time_s_label: str = "audio_tfr_time_s"

    # Barometer columns
    barometer_data_raw_label: str = "barometer_wf_raw"
    barometer_data_highpass_label: str = "barometer_wf_highpass"
    barometer_epoch_s_label: str = "barometer_epoch_s"
    barometer_fs_label: str = "barometer_sample_rate_hz"
    barometer_tfr_bits_label: str = "barometer_tfr_bits"
    barometer_tfr_frequency_hz_label: str = "barometer_tfr_frequency_hz"
    barometer_tfr_time_s_label: str = "barometer_tfr_time_s"

    # Accelerometer columns
    accelerometer_data_raw_label: str = "accelerometer_wf_raw"
    accelerometer_data_highpass_label: str = "accelerometer_wf_highpass"
    accelerometer_epoch_s_label: str = "accelerometer_epoch_s"
    accelerometer_fs_label: str = "accelerometer_sample_rate_hz"
    accelerometer_tfr_bits_label: str = "accelerometer_tfr_bits"
    accelerometer_tfr_frequency_hz_label: str = "accelerometer_tfr_frequency_hz"
    accelerometer_tfr_time_s_label: str = "accelerometer_tfr_time_s"

    # Gyroscope columns
    gyroscope_data_raw_label: str = "gyroscope_wf_raw"
    gyroscope_data_highpass_label: str = "gyroscope_wf_highpass"
    gyroscope_epoch_s_label: str = "gyroscope_epoch_s"
    gyroscope_fs_label: str = "gyroscope_sample_rate_hz"
    gyroscope_tfr_bits_label: str = "gyroscope_tfr_bits"
    gyroscope_tfr_frequency_hz_label: str = "gyroscope_tfr_frequency_hz"
    gyroscope_tfr_time_s_label: str = "gyroscope_tfr_time_s"

    # Magnetometer columns
    magnetometer_data_raw_label: str = "magnetometer_wf_raw"
    magnetometer_data_highpass_label: str = "magnetometer_wf_highpass"
    magnetometer_epoch_s_label: str = "magnetometer_epoch_s"
    magnetometer_fs_label: str = "magnetometer_sample_rate_hz"
    magnetometer_tfr_bits_label: str = "magnetometer_tfr_bits"
    magnetometer_tfr_frequency_hz_label: str = "magnetometer_tfr_frequency_hz"
    magnetometer_tfr_time_s_label: str = "magnetometer_tfr_time_s"

    # Load data
    df_skyfall_data = sf_dw.dw_main(tfr_config.tfr_load_method)

    # Start TFR plots
    print("\nInitiating time-frequency representation of Skyfall:")
    print(f"tfr_type: {tfr_config.tfr_type}, order: {tfr_config.tfr_order_number_N}")

    # Get the station id
    station_id_str = df_skyfall_data[station_label][0]

    # Microphone sensor stats
    print(f'\nmic_sample_rate_hz: {df_skyfall_data[audio_fs_label][0]}'
          f'\nmic_epoch_s_0: {df_skyfall_data[audio_epoch_s_label][0][0]}')

    # Frame to mic start and end and plots
    event_reference_time_epoch_s = df_skyfall_data[audio_epoch_s_label][0][0]

    # Calculate Time Frequency Representation for microphone
    print('Starting tfr_bits_panda for mic:')
    df_skyfall_data = rpd_tfr.tfr_bits_panda(df=df_skyfall_data,
                                             sig_wf_label=audio_data_label,
                                             sig_sample_rate_label=audio_fs_label,
                                             order_number_input=tfr_config.tfr_order_number_N,
                                             tfr_type=tfr_config.tfr_type,
                                             new_column_tfr_bits=audio_tfr_bits_label,
                                             new_column_tfr_frequency_hz=audio_tfr_frequency_hz_label,
                                             new_column_tfr_time_s=audio_tfr_time_s_label)
    # Plot microphone TFR
    pnl.plot_wf_mesh_vert(redvox_id=station_id_str,
                          wf_panel_2_sig=df_skyfall_data[audio_data_label][0],
                          wf_panel_2_time=df_skyfall_data[audio_epoch_s_label][0],
                          mesh_time=df_skyfall_data[audio_tfr_time_s_label][0],
                          mesh_frequency=df_skyfall_data[audio_tfr_frequency_hz_label][0],
                          mesh_panel_0_tfr=df_skyfall_data[audio_tfr_bits_label][0],
                          figure_title=skyfall_config.event_name +
                                       f": Audio, {tfr_config.tfr_type.upper()} and waveform",
                          start_time_epoch=event_reference_time_epoch_s,
                          mesh_panel_0_color_range=tfr_config.mc_range['Audio'],
                          mesh_panel_0_colormap_scaling=tfr_config.mc_scale['Audio'],
                          figure_title_show=tfr_config.show_fig_titles,
                          wf_panel_2_units="Audio, Norm")

    # Barometer sensor stats
    print(f'\nbarometer_sample_rate_hz: {df_skyfall_data[barometer_fs_label][0]}'
          f'\nbarometer_epoch_s_0: {df_skyfall_data[barometer_epoch_s_label][0][0]}')

    barometer_tfr_start_epoch: float = df_skyfall_data[barometer_epoch_s_label][0][0]  # first timestamp
    if tfr_config.sensor_hp['Bar']:
        bar_sig_label, bar_hp_raw = barometer_data_highpass_label, 'hp'
    else:
        bar_sig_label, bar_hp_raw = barometer_data_raw_label, 'raw'

    # Calculate Time Frequency Representation for barometer
    print('Starting tfr_bits_panda for barometer:')
    df_skyfall_data = rpd_tfr.tfr_bits_panda(df=df_skyfall_data,
                                             sig_wf_label=bar_sig_label,
                                             sig_sample_rate_label=barometer_fs_label,
                                             order_number_input=tfr_config.tfr_order_number_N,
                                             tfr_type=tfr_config.tfr_type,
                                             new_column_tfr_bits=barometer_tfr_bits_label,
                                             new_column_tfr_frequency_hz=barometer_tfr_frequency_hz_label,
                                             new_column_tfr_time_s=barometer_tfr_time_s_label)

    # Plot barometer TFR
    pnl.plot_wf_mesh_vert(redvox_id=station_id_str,
                          wf_panel_2_sig=df_skyfall_data[bar_sig_label][0][0],
                          wf_panel_2_time=df_skyfall_data[barometer_epoch_s_label][0],
                          mesh_time=df_skyfall_data[barometer_tfr_time_s_label][0][0],
                          mesh_frequency=df_skyfall_data[barometer_tfr_frequency_hz_label][0][0],
                          mesh_panel_0_tfr=df_skyfall_data[barometer_tfr_bits_label][0][0],
                          mesh_panel_0_colormap_scaling=tfr_config.mc_scale["Bar"],
                          mesh_panel_0_color_range=tfr_config.mc_range["Bar"],
                          figure_title=skyfall_config.event_name +
                                       f": Barometer, {tfr_config.tfr_type.upper()} and waveform",
                          start_time_epoch=barometer_tfr_start_epoch,
                          figure_title_show=tfr_config.show_fig_titles,
                          wf_panel_2_units=f"Bar {bar_hp_raw}, kPa")

    # Acceleration sensor stats
    print(f'\naccelerometer_sample_rate_hz: {df_skyfall_data[accelerometer_fs_label][0]}'
          f'\naccelerometer_epoch_s_0: {df_skyfall_data[accelerometer_epoch_s_label][0][0]}')

    acceleromter_tfr_start_epoch: float = df_skyfall_data[accelerometer_epoch_s_label][0][0]  # first timestamp
    if tfr_config.sensor_hp['Acc']:
        acc_sig_label, acc_hp_raw = accelerometer_data_highpass_label, 'hp'
    else:
        acc_sig_label, acc_hp_raw = accelerometer_data_raw_label, 'raw'

    # Calculate Time Frequency Representation for accelerometer
    print('Starting tfr_bits_panda for 3 channel acceleration:')
    df_skyfall_data = rpd_tfr.tfr_bits_panda(df=df_skyfall_data,
                                             sig_wf_label=acc_sig_label,
                                             sig_sample_rate_label=accelerometer_fs_label,
                                             order_number_input=tfr_config.tfr_order_number_N,
                                             tfr_type=tfr_config.tfr_type,
                                             new_column_tfr_bits=accelerometer_tfr_bits_label,
                                             new_column_tfr_frequency_hz=accelerometer_tfr_frequency_hz_label,
                                             new_column_tfr_time_s=accelerometer_tfr_time_s_label)
    # Plot X, Y, Z accelerometer TFR
    for ax_n in range(3):
        pnl.plot_wf_mesh_vert(redvox_id=station_id_str,
                              wf_panel_2_sig=df_skyfall_data[acc_sig_label][0][ax_n],
                              wf_panel_2_time=df_skyfall_data[accelerometer_epoch_s_label][0],
                              mesh_time=df_skyfall_data[accelerometer_tfr_time_s_label][0][ax_n],
                              mesh_frequency=df_skyfall_data[accelerometer_tfr_frequency_hz_label][0][ax_n],
                              mesh_panel_0_tfr=df_skyfall_data[accelerometer_tfr_bits_label][0][ax_n],
                              mesh_panel_0_colormap_scaling=tfr_config.mc_scale["Acc"],
                              mesh_panel_0_color_range=tfr_config.mc_range["Acc"],
                              figure_title=skyfall_config.event_name +
                                           f": Accelerometer, {tfr_config.tfr_type.upper()} and waveform",
                              start_time_epoch=acceleromter_tfr_start_epoch,
                              figure_title_show=tfr_config.show_fig_titles,
                              wf_panel_2_units=f"Acc {axes[ax_n]} {acc_hp_raw}, m/$s^2$")

    # Gyroscope sensor stats
    print(f'\ngyroscope_sample_rate_hz: {df_skyfall_data[gyroscope_fs_label][0]}'
          f'\ngyroscope_epoch_s_0: {df_skyfall_data[gyroscope_epoch_s_label][0][0]}')

    gyroscope_tfr_start_epoch: float = df_skyfall_data[gyroscope_epoch_s_label][0][0]  # first timestamp
    if tfr_config.sensor_hp['Gyr']:
        gyr_sig_label, gyr_hp_raw = gyroscope_data_highpass_label, 'hp'
    else:
        gyr_sig_label, gyr_hp_raw = gyroscope_data_raw_label, 'raw'

    # Calculate Time Frequency Representation for gyroscope
    print('Starting tfr_bits_panda for 3 channel gyroscope:')
    df_skyfall_data = rpd_tfr.tfr_bits_panda(df=df_skyfall_data,
                                             sig_wf_label=gyr_sig_label,
                                             sig_sample_rate_label=gyroscope_fs_label,
                                             order_number_input=tfr_config.tfr_order_number_N,
                                             tfr_type=tfr_config.tfr_type,
                                             new_column_tfr_bits=gyroscope_tfr_bits_label,
                                             new_column_tfr_frequency_hz=gyroscope_tfr_frequency_hz_label,
                                             new_column_tfr_time_s=gyroscope_tfr_time_s_label)
    # Plot X, Y, Z gyroscope TFR
    for ax_n in range(3):
        pnl.plot_wf_mesh_vert(redvox_id=station_id_str,
                              wf_panel_2_sig=df_skyfall_data[gyr_sig_label][0][ax_n],
                              wf_panel_2_time=df_skyfall_data[gyroscope_epoch_s_label][0],
                              mesh_time=df_skyfall_data[gyroscope_tfr_time_s_label][0][ax_n],
                              mesh_frequency=df_skyfall_data[gyroscope_tfr_frequency_hz_label][0][ax_n],
                              mesh_panel_0_tfr=df_skyfall_data[gyroscope_tfr_bits_label][0][ax_n],
                              mesh_panel_0_colormap_scaling=tfr_config.mc_scale["Gyr"],
                              mesh_panel_0_color_range=tfr_config.mc_range["Gyr"],
                              figure_title=skyfall_config.event_name +
                                           f": Gyroscope, {tfr_config.tfr_type.upper()} and waveform",
                              start_time_epoch=gyroscope_tfr_start_epoch,
                              figure_title_show=tfr_config.show_fig_titles,
                              wf_panel_2_units=f"Gyr {axes[ax_n]} {gyr_hp_raw}, rad/s")

    # Magnetometer sensor stats
    print(f'\nmagnetometer_sample_rate_hz: {df_skyfall_data[magnetometer_fs_label][0]}'
          f'\nmagnetometer_epoch_s_0: {df_skyfall_data[magnetometer_epoch_s_label][0][0]}')

    magnetometer_tfr_start_epoch: float = df_skyfall_data[magnetometer_epoch_s_label][0][0]  # first timestamp
    if tfr_config.sensor_hp['Mag']:
        mag_sig_label, mag_hp_raw = magnetometer_data_highpass_label, 'hp'
    else:
        mag_sig_label, mag_hp_raw = magnetometer_data_raw_label, 'raw'

    # Calculate Time Frequency Representation for magnetometer
    print('Starting tfr_bits_panda for 3 channel magnetometer:')
    df_skyfall_data = rpd_tfr.tfr_bits_panda(df=df_skyfall_data,
                                             sig_wf_label=mag_sig_label,
                                             sig_sample_rate_label=magnetometer_fs_label,
                                             order_number_input=tfr_config.tfr_order_number_N,
                                             tfr_type=tfr_config.tfr_type,
                                             new_column_tfr_bits=magnetometer_tfr_bits_label,
                                             new_column_tfr_frequency_hz=magnetometer_tfr_frequency_hz_label,
                                             new_column_tfr_time_s=magnetometer_tfr_time_s_label)

    # Plot X, Y, Z magnetometer TFR
    for ax_n in range(3):
        pnl.plot_wf_mesh_vert(redvox_id=station_id_str,
                              wf_panel_2_sig=df_skyfall_data[mag_sig_label][0][ax_n],
                              wf_panel_2_time=df_skyfall_data[magnetometer_epoch_s_label][0],
                              mesh_time=df_skyfall_data[magnetometer_tfr_time_s_label][0][ax_n],
                              mesh_frequency=df_skyfall_data[magnetometer_tfr_frequency_hz_label][0][ax_n],
                              mesh_panel_0_tfr=df_skyfall_data[magnetometer_tfr_bits_label][0][ax_n],
                              mesh_panel_0_colormap_scaling=tfr_config.mc_scale["Mag"],
                              mesh_panel_0_color_range=tfr_config.mc_range["Mag"],
                              figure_title=skyfall_config.event_name +
                                           f": Magnetometer, {tfr_config.tfr_type.upper()} and waveform",
                              start_time_epoch=magnetometer_tfr_start_epoch,
                              figure_title_show=tfr_config.show_fig_titles,
                              wf_panel_2_units=f"Mag {axes[ax_n]} {mag_hp_raw}, $\mu$T")

    # Plot TFR all sensor waveforms
    rpd_plot.plot_mesh_pandas(df=df_skyfall_data,
                              mesh_time_label=[audio_tfr_time_s_label,
                                               barometer_tfr_time_s_label,
                                               accelerometer_tfr_time_s_label,
                                               gyroscope_tfr_time_s_label,
                                               magnetometer_tfr_time_s_label],
                              mesh_frequency_label=[audio_tfr_frequency_hz_label,
                                                    barometer_tfr_frequency_hz_label,
                                                    accelerometer_tfr_frequency_hz_label,
                                                    gyroscope_tfr_frequency_hz_label,
                                                    magnetometer_tfr_frequency_hz_label],
                              mesh_tfr_label=[audio_tfr_bits_label,
                                              barometer_tfr_bits_label,
                                              accelerometer_tfr_bits_label,
                                              gyroscope_tfr_bits_label,
                                              magnetometer_tfr_bits_label],
                              t0_sig_epoch_s=df_skyfall_data[audio_epoch_s_label][0][0],
                              sig_id_label=["Audio", "Bar",
                                            "Acc X", "Acc Y", "Acc Z",
                                            'Gyr X', 'Gyr Y', 'Gyr Z',
                                            'Mag X', 'Mag Y', 'Mag Z'],
                              fig_title_show=tfr_config.show_fig_titles,
                              fig_title="",
                              frequency_scaling='log',
                              common_colorbar=False,
                              mesh_color_scaling=[tfr_config.mc_scale["Audio"], tfr_config.mc_scale["Bar"],
                                                  tfr_config.mc_scale["Acc"], tfr_config.mc_scale["Acc"],
                                                  tfr_config.mc_scale["Acc"],
                                                  tfr_config.mc_scale["Gyr"], tfr_config.mc_scale["Gyr"],
                                                  tfr_config.mc_scale["Gyr"],
                                                  tfr_config.mc_scale["Mag"], tfr_config.mc_scale["Mag"],
                                                  tfr_config.mc_scale["Mag"]],
                              mesh_color_range=[tfr_config.mc_range["Audio"], tfr_config.mc_range["Bar"],
                                                tfr_config.mc_range["Acc"], tfr_config.mc_range["Acc"],
                                                tfr_config.mc_range["Acc"],
                                                tfr_config.mc_range["Gyr"], tfr_config.mc_range["Gyr"],
                                                tfr_config.mc_range["Gyr"],
                                                tfr_config.mc_range["Mag"], tfr_config.mc_range["Mag"],
                                                tfr_config.mc_range["Mag"]],
                              ytick_values_show=True)

    plt.show()


if __name__ == "__main__":
    main()
