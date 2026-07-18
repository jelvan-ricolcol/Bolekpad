import re

with open('/home/runner/work/Bolekpad/Bolekpad/src/components/BolekSlides.tsx', 'r') as f:
    content = f.read()

watch_only_block_pattern = re.compile(
    r'(if \(isWatchOnly\) \{.*?return \(\n\s*)<div className="w-full min-h-\[500px\] flex-1 bg-stone-900 border border-stone-800 rounded-3xl p-6 flex flex-col justify-between select-none relative overflow-hidden">(.*?)</div>\n\s*\);\n\s*\}'
    , re.DOTALL
)

def repl(m):
    return """if (isWatchOnly) {
    const playSlide = project.slides[playIndex] || project.slides[0];
    return (
      <div className="fixed inset-0 bg-stone-950 z-[99999] flex flex-col justify-between p-6 md:p-8 select-none font-sans overflow-hidden">
        {/* Watching Banner - Premium Redesign */}
        <div className="flex items-center justify-between bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl px-6 py-4 text-stone-200 shadow-2xl mx-auto w-full max-w-[1000px]">
          <div className="flex items-center gap-4">
            <div className="flex items-center justify-center w-8 h-8 rounded-full bg-emerald-500/20">
              <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse" />
            </div>
            <div className="flex flex-col">
              <span className="text-sm font-black tracking-widest uppercase font-mono text-white">
                {project.title || 'Shared Presentation'}
              </span>
              <span className="text-[10px] text-stone-400 font-medium tracking-wide">
                Live Public View
              </span>
            </div>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-[11px] font-bold tracking-wider bg-white/10 text-white px-4 py-1.5 rounded-full border border-white/10 font-mono shadow-inner">
              Slide {playIndex + 1} <span className="text-stone-400 mx-1">/</span> {project.slides.length}
            </span>
          </div>
        </div>

        {/* Watch Only Slide Player Frame */}
        <div className="flex-1 flex items-center justify-center py-6 relative">
          <AnimatePresence mode="wait">
            <motion.div
              key={playSlide.id}
              initial={{ opacity: 0, y: 15, scale: 0.98 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: -15, scale: 0.98 }}
              transition={{ duration: 0.4, ease: 'easeOut' }}
              style={getSlideBgStyle(playSlide)}
              className="w-full max-w-[1000px] aspect-[16/9] rounded-2xl shadow-[0_30px_80px_rgba(0,0,0,0.6)] border border-white/10 relative overflow-hidden shrink-0 flex items-center justify-center p-4 ring-1 ring-white/5"
            >
              {playSlide.elements.map(el => {
                const isDark = playSlide.backgroundColor === '#1c1917' || playSlide.backgroundType === 'image';
                return (
                  <div
                    key={el.id}
                    style={{
                      left: `${el.x}%`,
                      top: `${el.y}%`,
                      width: `${el.width}%`,
                      height: `${el.height}%`,
                    }}
                    className="absolute flex items-center justify-center p-2 text-center"
                  >
                    {el.type === 'text' ? (
                      <p
                        style={{
                          fontSize: el.fontSize ? `${el.fontSize * 1.2}px` : '18px',
                          color: el.color || (isDark ? '#ffffff' : '#1c1917'),
                          fontWeight: el.fontStyle === 'bold' ? 'bold' : 'normal',
                          fontStyle: el.fontStyle === 'italic' ? 'italic' : 'normal'
                        }}
                        className="leading-relaxed whitespace-pre-wrap select-none tracking-tight font-sans drop-shadow-sm"
                      >
                        {el.content}
                      </p>
                    ) : el.type === 'image' ? (
                      <img
                        src={el.content}
                        alt="Slide asset"
                        className="w-full h-full object-contain rounded-xl shadow-md select-none pointer-events-none"
                        referrerPolicy="no-referrer"
                      />
                    ) : (
                      <iframe
                        src={getYoutubeEmbedUrl(el.content)}
                        className="w-full h-full rounded-xl shadow-xl border-0 ring-1 ring-black/5"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen
                        title="Shared YouTube element"
                      />
                    )}
                  </div>
                );
              })}
            </motion.div>
          </AnimatePresence>
        </div>

        {/* Interactive Play Controls */}
        <div className="flex items-center justify-center gap-6 py-4 shrink-0 mx-auto w-full max-w-[1000px] border-t border-white/10 mt-2">
          <button
            type="button"
            disabled={playIndex === 0}
            onClick={() => setPlayIndex(p => p - 1)}
            className="w-12 h-12 rounded-full bg-white/10 hover:bg-white/20 border border-white/10 text-white flex items-center justify-center disabled:opacity-30 disabled:hover:bg-white/10 cursor-pointer transition-all active:scale-90 shadow-lg backdrop-blur-sm"
            title="Previous"
          >
            <ChevronLeft className="w-6 h-6" />
          </button>

          <div className="flex gap-2.5 px-6 py-3 rounded-full bg-white/5 border border-white/10 backdrop-blur-md shadow-inner">
            {project.slides.map((_, i) => (
              <button
                key={i}
                type="button"
                onClick={() => setPlayIndex(i)}
                className={`w-2.5 h-2.5 rounded-full transition-all duration-300 shadow-sm ${i === playIndex ? 'bg-emerald-400 scale-125 ring-2 ring-emerald-400/30' : 'bg-white/30 hover:bg-white/60'}`}
              />
            ))}
          </div>

          <button
            type="button"
            disabled={playIndex === project.slides.length - 1}
            onClick={() => setPlayIndex(p => p + 1)}
            className="w-12 h-12 rounded-full bg-white/10 hover:bg-white/20 border border-white/10 text-white flex items-center justify-center disabled:opacity-30 disabled:hover:bg-white/10 cursor-pointer transition-all active:scale-90 shadow-lg backdrop-blur-sm"
            title="Next"
          >
            <ChevronRight className="w-6 h-6" />
          </button>
        </div>
      </div>
    );
  }"""

new_content = watch_only_block_pattern.sub(repl, content)

if new_content == content:
    print("No changes made. Regex might have failed.")
else:
    with open('/home/runner/work/Bolekpad/Bolekpad/src/components/BolekSlides.tsx', 'w') as f:
        f.write(new_content)
    print("Successfully patched watch mode layout.")
