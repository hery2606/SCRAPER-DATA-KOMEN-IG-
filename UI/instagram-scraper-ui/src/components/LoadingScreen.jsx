export default function LoadingScreen() {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60">
      
      <div className="relative w-80 p-8 rounded-2xl
        bg-white/10 backdrop-blur-xl
        border border-white/20
        shadow-[0_0_40px_rgba(0,245,255,0.3)]">

        {/* Neon Ring */}
        <div className="flex justify-center mb-6">
          <div className="w-16 h-16 rounded-full border-4
            border-neon border-t-transparent
            animate-spin shadow-[0_0_20px_rgba(0,245,255,0.8)]">
          </div>
        </div>

        {/* Text */}
        <h2 className="text-center text-xl font-bold text-neon mb-2">
          Scraping Instagram
        </h2>
        <p className="text-center text-gray-300 text-sm">
          Mengambil komentar & username...
        </p>
      </div>
    </div>
  );
}
