**Things to do :**



API key for Payroll

Physio net Dataset







**Things to be done before next review :**



* In depth info of literature review :
  -> Spectral Rendering \& RGB-to-Spectrum Conversion: - \*Smits, B.\* (1999). "An RGB-to-Spectrum Conversion for Reflectances." Journal of Graphics Tools, 4(4), 11-22.
  -> Anaglyph 3D \& Depth Mapping(2014): - "Depth-based 3D Anaglyph Image Modeling." IEEE Conference Proceedings.
  -> Strabismus \& VR Accessibility: Yang, Y., et al.\* (2023). "The effect of virtual reality technology in children after surgery for concomitant strabismus." Indian Journal of Ophthalmology, 71(2), 472-476.



* why we are using 31 bands only .. ??
  -> We selected 31 spectral bands because the visible spectrum spans approximately 390nm to 750nm, which gives a total range of about 360nm. Dividing this range into 31 bands results in a spacing of roughly 12nm between wavelengths. This spacing is smaller than the perceptual bandwidth of human cone cells, which typically respond over a 30–40nm range, meaning the human eye cannot distinguish variations finer than that. Therefore, sampling at 12nm ensures smooth and visually continuous spectral dispersion without noticeable banding. At the same time, increasing the number of bands significantly would linearly increase memory usage and computational cost, especially in a CPU-based real-time VR system, without producing perceptible visual improvement. Thus, 31 bands represent a balanced engineering decision that maintains perceptual accuracy while preserving real-time performance efficiency.



* what are other depth estimation other than neural networks, heuristic  depth?
  -> Apart from neural networks and heuristic depth, classical depth estimation methods include stereo triangulation, structure-from-motion, time-of-flight sensing, structured light, and geometric perspective-based methods. However, these approaches either require additional hardware, multiple viewpoints, heavy correspondence matching, or significant computational resources. Since our system is designed for real-time CPU-based VR processing and already performs spectral dispersion over 31 bands, integrating complex depth estimation methods would significantly increase latency and reduce feasibility. Heuristic depth estimation provides a lightweight, deterministic, and hardware-independent solution that enables efficient stereo synthesis while maintaining real-time performance, making it more suitable for our system constraints.
  -> Stereo Vision (Triangulation-Based)
  -> Structure from Motion (SfM)
  -> Time-of-Flight (ToF)
  -> Structured Light
  -> Monocular Geometric Methods
  -> Why Heuristic Depth Is Better for Your System :
  -> Computational Efficiency
  -> No Additional Hardware Required
  -> System Integration Simplicity



* what are the no of spacings between 390nm - 750nm :
  -> Between 390nm and 750nm : 750 - 390 = 360nm
  -> total spectral Range is 360nm
  -> if using 31 bands : NO of intervals is 31-1 = 30 spacings (no of spacing)
  360/30 = 12 nm per spacing
  -> if we have N bands the spacing is always N-1 Spacings.



* comparison between the o/p of NN and hurestic :



* -> Neural network-based depth estimation produces dense, object-aware, and highly realistic depth maps by learning spatial features from large datasets,      making it more accurate in complex scenes. However, it requires significant computational resources, typically GPU acceleration, and may introduce latency or inconsistencies depending on training data. In contrast, heuristic depth estimation relies on predefined geometric or intensity-based rules to approximate depth. While less accurate in capturing fine object boundaries, it is computationally lightweight, deterministic, hardware-independent, and more suitable for real-time CPU-based systems. For our VR spectral dispersion framework, heuristic depth provides a practical balance between perceptual effectiveness and computational feasibility.



* -> In our framework, depth estimation is primarily used to control stereo disparity and wavelength-dependent dispersion rather than to perform full 3D reconstruction. Neural network-based depth would produce more accurate object-level boundaries and occlusion handling, potentially improving geometric realism. However, it would significantly increase computational load and reduce real-time feasibility, especially since our system already performs 31-band spectral processing. The heuristic depth approach produces smooth, stable depth gradients that are sufficient to drive perceptually convincing stereo dispersion effects while maintaining low latency and CPU compatibility. Therefore, for our system objectives, heuristic depth provides a practical and efficient solution.
