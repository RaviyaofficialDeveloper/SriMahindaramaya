import os
import glob
import re

files = glob.glob('*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Navbar text
    content = content.replace(
        '<h2>ශ්‍රී මහින්දාරාම<br>විද්‍යායතන පිරිවෙන</h2>',
        '<h2>ශ්රී මහින්දාරා<br>විද්යායතන පිරිවෙන</h2>'
    )
    
    # 2. Footer text
    content = re.sub(
        r'<h3 style="margin-bottom: 0; color: white;">ශ්‍රී මහින්දාරාම<br>පිරිවෙන</h3>',
        '<h3 style="margin-bottom: 0; color: white;">ශ්රී මහින්දාරා<br>විද්යායතන පිරිවෙන</h3>',
        content
    )
    
    # 3. Footer tag line
    content = re.sub(
        r'<p class="sinhala-text">බුද්ධ ධර්මය සහ සිංහල සංස්කෘතිය ආරක්ෂා කරමින් අනාගත පරපුරට දායාද කිරීම අපගේ\s*අරමුණයි\.</p>',
        '<p class="sinhala-text">බුද්ධ ධර්මය සහ සිංහල සංස්කෘතිය ආරක්ෂා කරමින්...</p>',
        content,
        flags=re.MULTILINE
    )
    content = re.sub(
        r'<p class="sinhala-text">බුද්ධ ධර්මය සහ සිංහල සංස්කෘතිය ආරක්ෂා කරමින් අනාගත පරපුරට දායාද කිරීම අපගේ අරමුණයි\.</p>',
        '<p class="sinhala-text">බුද්ධ ධර්මය සහ සිංහල සංස්කෘතිය ආරක්ෂා කරමින්...</p>',
        content
    )
    
    # 4. Copyright
    # Find any copyright p tag and replace it.
    content = re.sub(
        r'<p>Copyright &copy; 2026 \| බුද්ධ ශාසනයේ චිරස්ථිතිය වෙනුවෙන් 🙏 \| Sri Mahindarama Vidyayathana Pirivena\s*</p>',
        '<p>Copyright &copy; 2026 | 🙏 <span style="color: var(--primary-color);">බුද්ධ ශාසනයේ චිරස්ථිතිය වෙනුවෙන්</span> | Sri Mahindarama Vidyayathana Pirivena</p>',
        content,
        flags=re.MULTILINE
    )

    # 5. Logo icon classes
    content = content.replace(
        'class="logo-icon"',
        'class="logo-icon chakra-spin"'
    )
    
    # 6. Hero specific
    if 'index.html' in filepath:
        content = content.replace(
            '<h1>ශ්‍රී මහින්දාරාම විද්‍යායතන පිරිවෙන</h1>',
            '<h1>ශ්රී මහින්දාරා විද්යායතන පිරිවෙන</h1>'
        )
        content = content.replace(
            '<div class="hero-bg" style="background-image: url(\'assets/images/hero_dharmachakra.png\');"></div>',
            '<div class="hero-bg" style="background-image: url(\'assets/images/hero_dharmachakra.png\');"></div>\n        <canvas id="hero-particles" style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:1; pointer-events: none;"></canvas>'
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all HTML files.")
