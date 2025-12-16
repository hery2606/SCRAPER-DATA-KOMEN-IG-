export default function SkeletonTable() {
  return (
    <div className="animate-pulse">
      <div className="overflow-hidden rounded-xl border border-white/10">
        <table className="w-full text-sm">
          <thead className="bg-black/60">
            <tr>
              <th className="px-4 py-3 text-left text-neon">Username</th>
              <th className="px-4 py-3 text-left text-neon">Komentar</th>
            </tr>
          </thead>
          <tbody>
            {Array.from({ length: 6 }).map((_, i) => (
              <tr key={i} className="border-t border-white/5">
                <td className="px-4 py-3">
                  <div className="h-4 w-24 rounded bg-white/20"></div>
                </td>
                <td className="px-4 py-3">
                  <div className="h-4 w-full rounded bg-white/20"></div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
