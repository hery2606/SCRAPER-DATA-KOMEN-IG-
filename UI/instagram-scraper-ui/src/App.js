import { useState } from "react";

export default function App() {
  const [url, setUrl] = useState("");
  const [comments, setComments] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const scrape = async () => {
    if (!url) {
      alert("Masukkan URL Instagram dulu!");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setComments([]);

      const res = await fetch(
        `http://127.0.0.1:8000/scrape?post_url=${encodeURIComponent(url)}`,
        { method: "POST" }
      );

      if (!res.ok) {
        throw new Error("Backend error");
      }

      const data = await res.json();
      setComments(data.comments);

    } catch (err) {
      console.error(err);
      setError("Gagal mengambil data dari backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-black via-gray-900 to-black">
      <div className="w-full max-w-5xl p-8 rounded-2xl
        bg-white/10 backdrop-blur-xl
        border border-white/20
        shadow-[0_0_40px_rgba(0,245,255,0.15)]">

        {/* HEADER */}
        <h1 className="text-3xl font-bold text-neon mb-2">
          Instagram Scraper
        </h1>

        {/* INPUT */}
        <div className="flex gap-4 mb-6">
          <input
            type="text"
            placeholder="Paste Instagram Post URL..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="flex-1 px-4 py-3 rounded-xl
              bg-black/40 text-white
              border border-white/20
              focus:outline-none focus:ring-2 focus:ring-neon"
          />

          <button
            onClick={scrape}
            disabled={loading}
            className="px-6 py-3 rounded-xl font-semibold
              bg-neon text-black
              hover:scale-105 transition
              disabled:opacity-50">
            {loading ? "Scraping..." : "Scrape"}
          </button>
        </div>

        {/* STATUS */}
        {error && (
          <p className="text-red-400 mb-4">{error}</p>
        )}

        {/* RESULT TABLE */}
        {comments.length > 0 && (
          <div className="max-h-[400px] overflow-y-auto rounded-xl
            border border-white/10">
            <table className="w-full text-sm">
              <thead className="sticky top-0 bg-black/60">
                <tr>
                  <th className="px-4 py-3 text-left text-neon">Username</th>
                  <th className="px-4 py-3 text-left text-neon">Komentar</th>
                </tr>
              </thead>
              <tbody>
                {comments.map((c, i) => (
                  <tr key={i}
                    className="border-t border-white/5 hover:bg-white/5">
                    <td className="px-4 py-2 text-neon font-semibold">
                      @{c.Username}
                    </td>
                    <td className="px-4 py-2 text-gray-300">
                      {c.Komentar}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {!loading && comments.length === 0 && (
          <p className="text-gray-400 text-center">
            Belum ada data
          </p>
        )}
      </div>
    </div>
  );
}
