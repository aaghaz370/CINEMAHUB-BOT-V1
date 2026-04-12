import React from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';
import { Play, Shield, Zap, Search, MonitorPlay, Film, Crown, Layers, Star, Download, Globe } from 'lucide-react';
import logoImg from '../assets/logo.png';
import netflixBanner from '../assets/netflix-banner.jpg'; // Keep this for aesthetic movie background

export default function Landing() {
  const BOT_LINK = "https://t.me/Univora_CinemahubBot";
  const SUPPORT_LINK = "https://t.me/rolexsir_8";

  const { scrollYProgress } = useScroll();
  const yBg = useTransform(scrollYProgress, [0, 1], ['0%', '50%']);
  const opacityBg = useTransform(scrollYProgress, [0, 0.5], [0.3, 0.05]);

  // Framer Variants
  const fadeUp = {
    hidden: { opacity: 0, y: 40 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }
  };

  const staggerContainer = {
    hidden: { opacity: 0 },
    visible: { opacity: 1, transition: { staggerChildren: 0.15 } }
  };

  return (
    <div className="min-h-screen bg-[#050505] text-white font-sans overflow-x-hidden selection:bg-red-500/30">
      
      {/* ── NAVBAR ── */}
      <nav className="fixed top-0 w-full z-50 bg-[#050505]/70 backdrop-blur-xl border-b border-white/5 transition-all">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          <div className="flex items-center gap-3 group cursor-pointer">
            <div className="relative">
              <div className="absolute inset-0 bg-red-600 blur-md opacity-0 group-hover:opacity-40 transition-opacity rounded-xl"></div>
              <img src={logoImg} alt="CinemaHub" className="w-10 h-10 rounded-xl relative z-10 border border-white/10 bg-[#0a0a0f] object-cover" />
            </div>
            <span className="font-black text-2xl tracking-tighter text-white drop-shadow-md">
              Cinema<span className="text-red-500">Hub</span>
            </span>
          </div>
          <div className="flex items-center gap-6">
            <a href="#features" className="hidden md:block text-sm font-semibold text-gray-400 hover:text-white transition-colors">Features</a>
            <a href="#premium" className="hidden md:block text-sm font-semibold text-gray-400 hover:text-red-400 transition-colors">Premium</a>
            <a href={BOT_LINK} target="_blank" rel="noopener noreferrer" 
               className="group relative inline-flex items-center justify-center px-6 py-2.5 font-bold text-white transition-all bg-red-600 rounded-full hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 focus:ring-offset-[#050505]">
               Launch Bot
            </a>
          </div>
        </div>
      </nav>

      {/* ── HERO ── */}
      <section className="relative min-h-[100dvh] pt-32 pb-20 flex flex-col items-center justify-center overflow-hidden">
        {/* Cinematic Background Parallax */}
        <motion.div style={{ y: yBg, opacity: opacityBg }} className="absolute inset-0 z-0">
          <div className="absolute inset-0 bg-gradient-to-b from-[#050505] via-transparent to-[#050505] z-10"></div>
          <div className="absolute inset-0 bg-gradient-to-r from-[#050505] via-transparent to-[#050505] z-10"></div>
          <img src={netflixBanner} alt="Hero" className="w-full h-full object-cover object-top scale-110" />
        </motion.div>
        
        {/* Glow Effects */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-red-700/20 blur-[120px] rounded-full pointer-events-none z-0"></div>

        <motion.div 
          variants={staggerContainer} initial="hidden" animate="visible" 
          className="relative z-10 w-full max-w-5xl mx-auto px-6 text-center"
        >
          <motion.div variants={fadeUp} className="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-red-500/30 bg-red-500/10 backdrop-blur-md mb-8">
             <Star className="w-4 h-4 text-red-500 fill-red-500 animate-pulse" />
             <span className="text-xs sm:text-sm font-bold text-red-300 tracking-wide uppercase">10 Million+ Movies & Anime Database</span>
          </motion.div>

          <motion.h1 variants={fadeUp} className="text-6xl md:text-8xl lg:text-[7.5rem] font-black tracking-tighter leading-[0.95] mb-8">
            The <span className="text-transparent bg-clip-text bg-gradient-to-br from-white via-gray-200 to-gray-500">Cinematic</span><br/>
            Experience.
          </motion.h1>

          <motion.p variants={fadeUp} className="text-lg md:text-2xl text-gray-400 max-w-2xl mx-auto font-medium leading-relaxed mb-12">
            Instantly search, stream, and download any movie, series, or cartoon. 
            All without limits, without waiting, and <span className="text-white font-bold">100% Free.</span>
          </motion.p>

          <motion.div variants={fadeUp} className="flex flex-col sm:flex-row items-center justify-center gap-5">
            <a href={BOT_LINK} target="_blank" rel="noopener noreferrer" 
               className="w-full sm:w-auto flex items-center justify-center gap-3 bg-white text-black px-8 py-4 rounded-full font-black text-lg hover:scale-105 transition-transform shadow-[0_0_40px_rgba(255,255,255,0.3)]">
              <Play className="fill-black w-5 h-5" /> Start Streaming
            </a>
            <a href="#premium" className="w-full sm:w-auto flex items-center justify-center gap-3 bg-transparent border border-white/20 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-white/5 transition-colors backdrop-blur-md">
              <Crown className="text-yellow-500 w-5 h-5" /> View Premium
            </a>
          </motion.div>
        </motion.div>
      </section>

      {/* ── BENTO GRID FEATURES ── */}
      <section id="features" className="py-24 px-6 max-w-7xl mx-auto relative z-10">
        <div className="mb-16">
          <h2 className="text-4xl md:text-5xl font-black tracking-tight mb-4">Beyond the Ordinary.</h2>
          <p className="text-xl text-gray-400">Everything you need, built right into the platform.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 auto-rows-[300px]">
          
          {/* Card 1: Huge Search */}
          <div className="md:col-span-2 md:row-span-2 bg-[#0d0d12] border border-white/5 rounded-3xl p-8 relative overflow-hidden group hover:border-red-500/30 transition-colors">
            <div className="absolute inset-0 bg-gradient-to-br from-red-600/5 to-transparent"></div>
            <Search className="w-12 h-12 text-red-500 mb-6" />
            <h3 className="text-3xl font-black tracking-tight mb-3">10M+ Database Search</h3>
            <p className="text-gray-400 text-lg max-w-md leading-relaxed">
              We indexed the entire Telegram network. Just type the name of the movie, anime, or series, and let CinemaHub find it instantly.
            </p>
            {/* Decorative UI element */}
            <div className="absolute right-[-10%] bottom-[-10%] w-72 h-72 bg-gradient-to-br from-[#13131c] to-[#0a0a0f] rounded-2xl border border-white/10 shadow-2xl flex flex-col p-4 group-hover:-translate-y-4 group-hover:-translate-x-4 transition-transform duration-500">
               <div className="w-full h-8 bg-white/5 rounded-lg mb-3 flex items-center px-3"><span className="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span><span className="text-xs text-gray-500 ml-2">Searching "Inception"...</span></div>
               <div className="w-full flex-1 bg-white/5 rounded-lg mb-2"></div>
               <div className="w-full flex-1 bg-white/5 rounded-lg"></div>
            </div>
          </div>

          {/* Card 2 */}
          <div className="bg-[#0d0d12] border border-white/5 rounded-3xl p-8 relative overflow-hidden group hover:border-yellow-500/30 transition-colors flex flex-col justify-between">
            <div>
              <Zap className="w-10 h-10 text-yellow-500 mb-4" />
              <h3 className="text-2xl font-bold tracking-tight mb-2">Zero Bandwidth Throttling</h3>
              <p className="text-gray-400 text-sm">Download and stream with blazing fast CDN edge servers.</p>
            </div>
            <div className="text-6xl font-black text-white/5">∞</div>
          </div>

          {/* Card 3 */}
          <div className="bg-[#0d0d12] border border-white/5 rounded-3xl p-8 relative overflow-hidden group hover:border-blue-500/30 transition-colors">
            <MonitorPlay className="w-10 h-10 text-blue-500 mb-4" />
            <h3 className="text-2xl font-bold tracking-tight mb-2">Native Player Engine</h3>
            <p className="text-gray-400 text-sm">Built-in theater mode, PiP, and deep link intents directly to VLC or MX Player.</p>
          </div>

          {/* Card 4 (Spans 2 cols on tablet) */}
          <div className="md:col-span-2 bg-[#0d0d12] border border-white/5 rounded-3xl p-8 relative overflow-hidden group hover:border-purple-500/30 transition-colors flex items-center">
             <div className="flex-1">
                <Globe className="w-10 h-10 text-purple-500 mb-4" />
                <h3 className="text-2xl font-bold tracking-tight mb-2">Cross-Device Sync</h3>
                <p className="text-gray-400 text-sm max-w-sm">Start watching on your phone, seamlessly continue exactly where you left off on your PC.</p>
             </div>
             <div className="hidden sm:block opacity-20 group-hover:opacity-100 transition-opacity relative">
                 <Shield className="w-32 h-32 text-purple-500" />
                 <Lock className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 text-white" />
             </div>
          </div>

        </div>
      </section>

      {/* ── HOW IT WORKS ── */}
      <section className="py-24 bg-gradient-to-b from-transparent to-[#08080c] relative">
        <div className="max-w-5xl mx-auto px-6">
          <div className="text-center mb-16">
             <h2 className="text-4xl font-black tracking-tight mb-4">Stream in 3 Steps.</h2>
          </div>
          
          <div className="relative">
            {/* Connecting line */}
            <div className="hidden md:block absolute left-12 top-10 bottom-10 w-0.5 bg-gradient-to-b from-red-600 via-red-900 to-transparent"></div>

            <div className="space-y-12">
              {[
                { num: "1", title: "Launch Remote Bot", desc: "Open the CinemaHub bot on Telegram. It acts as your personalized remote control for our servers." },
                { num: "2", title: "Search or Forward", desc: "Type any movie name. We scan our 10M+ database and instantly provide you with a secure web link." },
                { num: "3", title: "Grab Popcorn & Watch", desc: "Click the link. No ads, no popups. Instant high-quality streaming natively in your browser." }
              ].map((step, i) => (
                <div key={i} className="flex gap-6 md:gap-12 relative items-start group">
                  <div className="w-16 h-16 shrink-0 rounded-2xl bg-[#1a1a24] border border-white/10 flex items-center justify-center text-2xl font-black text-red-500 z-10 shadow-[0_0_20px_rgba(229,9,20,0)] group-hover:shadow-[0_0_20px_rgba(229,9,20,0.3)] transition-shadow">
                    {step.num}
                  </div>
                  <div className="pt-3">
                    <h3 className="text-2xl font-bold tracking-tight mb-3 text-white group-hover:text-red-400 transition-colors">{step.title}</h3>
                    <p className="text-lg text-gray-400 leading-relaxed max-w-xl">{step.desc}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ── PREMIUM UPGRADE ROW ── */}
      <section id="premium" className="py-24 px-6 relative overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-yellow-900/10 via-[#050505] to-[#050505]"></div>
        
        <div className="max-w-6xl mx-auto bg-gradient-to-br from-[#141411] to-[#0a0a0a] border border-yellow-500/20 rounded-[2.5rem] p-8 md:p-16 relative overflow-hidden">
          {/* Shine effect */}
          <div className="absolute top-0 right-0 w-full h-full bg-gradient-to-bl from-yellow-500/10 to-transparent pointer-events-none"></div>

          <div className="flex flex-col md:flex-row items-center gap-12 relative z-10">
            <div className="flex-1">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-yellow-500/10 border border-yellow-500/30 text-yellow-500 text-xs font-bold uppercase tracking-wider mb-6">
                 <Crown size={14} /> CinemaHub Premium
              </div>
              <h2 className="text-4xl md:text-5xl font-black tracking-tight mb-6 text-white">Upgrade Your Arsenal.</h2>
              <ul className="space-y-4 mb-10">
                {[
                  "Direct Browser Download (High Speed)",
                  "Zero Banner & Pop-Up Ads",
                  "Access to Exclusive Market New Content",
                  "Priority Request Processing",
                  "Advanced Sleep Timers & Themed UI"
                ].map((ft, i) => (
                  <li key={i} className="flex items-center gap-3 text-gray-300 font-medium">
                    <div className="w-5 h-5 rounded-full bg-yellow-500/20 flex items-center justify-center shrink-0">
                       <CheckCircle2 size={12} className="text-yellow-500" />
                    </div>
                    {ft}
                  </li>
                ))}
              </ul>
              <a href={SUPPORT_LINK} target="_blank" rel="noopener noreferrer" 
                 className="inline-flex items-center justify-center gap-2 bg-yellow-500 text-black px-8 py-4 rounded-full font-black text-lg hover:bg-yellow-400 hover:scale-105 transition-all shadow-[0_0_30px_rgba(234,179,8,0.3)]">
                Upgrade Now from ₹20
              </a>
            </div>

            <div className="flex-1 w-full relative h-[300px] hidden md:block">
               {/* Visual premium cards overlaying each other */}
               <div className="absolute top-10 right-20 w-64 h-64 bg-yellow-500/5 backdrop-blur-md border border-yellow-500/20 rounded-3xl transform rotate-6 animate-pulse"></div>
               <div className="absolute top-0 right-10 w-64 h-64 bg-gradient-to-br from-[#1a1a17] to-[#0d0d0c] border border-yellow-500/30 rounded-3xl transform -rotate-3 p-6 shadow-2xl flex flex-col justify-center items-center text-center">
                  <Crown className="w-16 h-16 text-yellow-500 mb-4" />
                  <h4 className="text-2xl font-black text-white mb-2">Max Plan</h4>
                  <p className="text-gray-400 text-sm">60 Days of absolute power.</p>
               </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── FOOTER ── */}
      <footer className="border-t border-white/5 bg-[#050505] pt-20 pb-10">
        <div className="max-w-7xl mx-auto px-6 text-center flex flex-col items-center">
          <img src={logoImg} className="w-12 h-12 rounded-xl mb-6 bg-white object-contain opacity-80 hover:opacity-100 transition-opacity" alt="CinemaHub" />
          <h2 className="text-3xl font-black tracking-tight mb-2 text-white">CinemaHub</h2>
          <p className="text-gray-500 font-medium mb-10 max-w-md">Engineered for speed, built for the viewers. The definitive Telegram streaming experience.</p>
          
          <div className="w-full flex flex-col md:flex-row items-center justify-between pt-8 border-t border-white/5 text-sm font-semibold text-gray-600 gap-4">
            <p>© 2026 CinemaHub. Powered by Univora.</p>
            <p className="flex items-center gap-1">Developed by <a href={SUPPORT_LINK} target="_blank" rel="noopener noreferrer" className="text-white hover:text-red-400 transition-colors">Rolex Sir</a></p>
          </div>
        </div>
      </footer>

    </div>
  );
}

// Minimal missing icons
function CheckCircle2(props) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/>
      <path d="M9 12l2 2 4-4"/>
    </svg>
  );
}
function Lock(props) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
      <path d="M7 11V7a5 5 0 0110 0v4"></path>
    </svg>
  );
}
