# thermal_study
thermal_image.py is for making the 2D pictures with the same range of temperature. To run it:
  
  python thermal_image.py  <input directory> <max temperature> <min temperature>
  e.g. python thermal_image.py  '/Users/xuanchen/Desktop/06_09_2021_11_42_42_RTD_bath5C_runaway/' 27 0
  
thermal_image_1d.py is for plotting temperature vs time plot for five points on the thermal images(four around the RTD and one far away from the heater). To run it:
  
  python thermal_image_1d.py  <input directory>
  e.g. python thermal_image_1d.py  '/Users/xuanchen/Desktop/06_09_2021_11_42_42_RTD_bath5C_runaway/'
  
thermal_image_RTD.py is for plotting temperature vs time plot for expected RTD value from the thermal image and the real RTD measurement. This is used to compare the performance between the thermal camera and the RTD. To run it:
  
  python thermal_image_RTD.py  <input directory>
  e.g. python thermal_image_RTD.py  '/Users/xuanchen/Desktop/06_09_2021_11_42_42_RTD_bath5C_runaway/'
